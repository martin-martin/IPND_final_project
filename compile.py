import os
import webapp2
import jinja2
from datetime import datetime
from google.appengine.ext import ndb
import re
import json


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
template_loader = jinja2.FileSystemLoader(template_dir)
# setting autoescape, an in-built feature in jinja2 that will escape HTML text coming from my content.py
# text input. Through this I can make my website more secure and provide a better user experience.
template_env = jinja2.Environment(loader = template_loader, autoescape = True)

class Handler(webapp2.RequestHandler):
    """contains the basic methods for rendering the templates into html pages"""
    def write(self, *arguments, **kw_arguments):
        """writes the content to a webpage, default as text/html"""
        self.response.out.write(*arguments, **kw_arguments)

    def render_str(self, template, **kw_arguments):
        """loads the specified template and renders the text"""
        t = template_env.get_template(template)
        return t.render(kw_arguments)

    def render(self, template, **kw_arguments):
        """calls the write function on the specified template's rendered text"""
        self.write(self.render_str(template, **kw_arguments))

######################################### HOMEPAGE ####################################################

class HomePage(Handler):
    """renders my landing page that gives an overview and navigation to the rest of the projects"""
    def get(self):
        self.render("/homepage_tem.html")

    def post(self):
        message = "Thank you for your feedback! :)"
        error = "I'll only record it if you write something ;)"
        comment = self.request.get("comments")
        if (not comment) or comment.isspace():
            self.render("/homepage_tem.html", error = error)
        else:
            new_comment = Comment(comment = comment)
            new_comment.put()
            self.render("/homepage_tem.html", message = message)

class Comment(ndb.Model):
    """collects the comments people leave and adds them to the datastore"""
    comment = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add = True)


##################################### RE-MADE STAGE 0-2 ###############################################

class StagePages(Handler):
    """renders my templates for the stages 0-2 and creates the individual webpages"""
    def get(self, regex):
        # load the data from the json file
        pages_tems_dict = json.load(open("data/pages_tems.json"))
        # create the links in the header:
        # if it's a special page (not in the list), link them to home
        back, forward = "/", "/"
        # check all elements in the page list
        for count, p in enumerate(pages_tems_dict["page_list"]):
            # if the current page is found
            if p == regex:
                # assign "back" to one index before and "forward" to one index place after current page
                back = pages_tems_dict["page_list"][count-1]
                forward = pages_tems_dict["page_list"][count+1]
        if regex == "stage3":
            back = "stage2"
            forward = "/stage3/re-use"
        elif regex == "stage4":
            back = "stage3"
            forward = "/stage4/"
        elif regex == "stage5":
            back = "stage4"
            forward = "/stage5/javascript"
        self.render(pages_tems_dict[regex]["template"], stage = pages_tems_dict[regex].get("stage"),
            back = back, forward = forward)


########################################### STAGE 3 ###################################################

class ReUse(Handler):
    """to make the page with information about code re-use"""
    def get(self):
        stage3_dict = json.load(open("data/s3_content.json"))
        links = stage3_dict.get("links")
        self.render("/stage3/re-use_tem.html", links=links, percent=60)

class OOPInfo(Handler):
    """to make the page with information about OOP"""
    def get(self):
        stage3_dict = json.load(open("data/s3_content.json"))
        text = stage3_dict.get("text")
        definitions = stage3_dict.get("definitions")
        self.render("/stage3/definitions_tem.html", content=text, definitions=definitions, percent=61)

class Finish(Handler):
    """to make the last page with nearly no information on it"""
    def get(self):
        stage3_dict = json.load(open("data/s3_content.json"))
        self.render("/stage3/finish_tem.html", percent=62)


########################################### STAGE 4 ###################################################

class FormPage(Handler):
    """creates the page with the empty forms, that prompt the visitor for input"""
    def get(self):
        topics = ["your thoughts about servers", "your thoughts about templates", "your thoughts about escaping and validation",
                "what did you find especially interesting", "was there something that made you smile?"]
        self.render('stage4/form_tem.html', topics = topics)


class UserPage(Handler):
    def get(self):
        # allows to access all the Page objects' parameters from the datastore
        query = Page.query().order(Page.post_date)
        # assigning variable names to the variables of the Page object
        for i in query:
            topics = i.topics
            content = i.content
            name = i.name
            date = i.date
            css = i.css
            smile = i.smile
        # calling the render function with the arguments to display the page
        self.render('stage4/page_tem.html', topics = topics, content = content, name = name,
            date = date, css = css, smile = smile)

    def post(self):
        # the code following here gets the value of a query parameter
        name = self.request.get("name")
        css = self.request.get("css")
        smile = self.request.get("smile")
        # inserts the current time as a timestamp when the page got created
        date = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M') + " (UTC)"
        # these are the headings that will display above the user's content
        topics = ["A micro guide to Servers", "Templating HTML", "Escaping troubles through Escaping and Validation",
                "! this was very interesting !", "* this made me smile *"]
        # get_all collects all the values of the specified query parameter and unifies them into a list
        paragraphs = self.request.get_all("content")
        # the next lines including the loop create a dictionary mapping the topics as keys to the paragraphs as values
        content = {}
        # a cool way of iterating with a for loop with index! thanks to my 2nd reviewer :)
        for index, topic in enumerate(topics):
            content[topic] = paragraphs[index]
        # sets the blank value to False by default, then tests if the name field is filled only by blanks
        blank = False
        if name.isspace():
            # if it's only blanks, it renders the form page again displaying an error message
            blank = True
            self.render('stage4/form_tem.html', topics = topics, blank = blank)
        # if all the necessary values are present, and name is not blank, instantiate a Page object
        elif name and date and topics and content and css and smile:
            input_page = Page(name = name, date = date, topics = topics, content = content,
             css = css, smile = smile)
            # add it to the datastore
            input_page.put()
            # allow a bit of time for the database to update
            import time
            delay_time = .1
            time.sleep(delay_time)
            # go to the page created by the user
            self.redirect('/stage4/userpage')
        # if necessary values are missing, redirect to a page displaying an error message
        else:
            self.redirect('/stage4/error')


class Collection(Handler):
    """this page collects all individual entries from the different users and puts them on one page"""
    def get(self):
        # this retrieves my objects from the datastore and sorts them in descending order (-)
        pages = Page.query().order(-Page.post_date)
        # I pass this variable that is a collection of all the user pages (objects) to my template
        # there I can iterate over them and create the individual pages (cool!)
        self.render('stage4/collection_tem.html', pages = pages)


class ErrorHandler(Handler):
    """displays an error message if instantiating the object fails"""
    def get(self):
        self.render('stage4/error_tem.html')


class Page(ndb.Model):
    """this is the Class that defines an object that will contain all the information that the user provides
    and that I will store on google data store and further use to display the individual pages on /collection."""
    # first two arguments are a list and a dictionary, therefore I need to use a different property.
    # topics (which is a list) can be made by using the repeated property.
    # I also tried the suggestion with content (which is a dict), however this does not work (PickleProperty does).
    topics = ndb.StringProperty(repeated=True)
    content = ndb.PickleProperty()
    name = ndb.StringProperty()
    css = ndb.StringProperty()
    smile = ndb.StringProperty()
    date = ndb.StringProperty()
    # this adds a timestamp to the generated object, about when it was created and stored.
    post_date = ndb.DateTimeProperty(auto_now_add = True)


########################################### STAGE 5 ###################################################

class InfoPage(Handler):
    """makes up the page that displays my notes about JS and the IPND progress bar"""
    def get(self):
        title = "MY NOTES ABOUT JAVASCRIPT"
        content = json.load(open("data/s5_about_js.json"))
        self.render('/stage5/stage5_main_tem.html', title = title, content = content)


#######################################################################################################


app = webapp2.WSGIApplication([
    # TODO: how to make the regex also accept the "/" character?
    # TODO: how to search for everything except some things, so I wouldn't need the /r/ part in the URL
    ('/', HomePage),
    ('/r/(\w+)', StagePages),
    ('/stage3/re-use', ReUse),
    ('/stage3/info', OOPInfo),
    ('/stage3/finish', Finish),
    ('/stage4/', FormPage),
    ('/stage4/userpage', UserPage),
    ('/stage4/collection', Collection),
    ('/stage4/error', ErrorHandler),
    ('/stage5/javascript', InfoPage)
], debug=True)
# debug = True means it writes out the errors onto my page, in case some occur