# In this file I auto-generate my webpages for the Stage 3 submission. For this I am using
# Class concepts and some knowledge about HTML templates that I learned in the videos for Stage 4.
# I did, however, not simply copy that code but looked through it and adapted it so I would
# understand it and that it it would fit for what I am doing here.

import os
import jinja2
import content


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
template_loader = jinja2.FileSystemLoader(template_dir)
# I set autoescape =  False for this project, because there are a few HTML tags that I have included in
# my content strings, that I want to be rendered as HTML tags. I understand that this is not a good
# practice when creating a website and in Stage 4 I will make this different.
## In case you have suggestions how to better store my content, so that formatting would not have to be
## done inside the strings and I could set autoescape = True without losing on formatting options:
## please do tell!
template_env = jinja2.Environment(loader = template_loader, autoescape = False)


class Handler(object):
	"""contains the basic methods for rendering the templates into html pages"""

	def render_str(self, template, **parameters):
		t = template_env.get_template(template)
		return t.render(parameters)

	def make_page(self, template):
		filename = template[:-5] + "_page.html"
		f = open(filename, "w")
		f.write(str(self.get()))


# the following Classes inherit te two methods from the Handler Class
class ReUse(Handler):
	"""to make the page with information about code re-use"""
	def get(self):
		links = content.links
		return self.render_str("/re-use.html", links=links, percent=60)

class OOPInfo(Handler):
	"""to make the page with information about OOP"""
	def get(self):
		text = content.text
		definitions = content.definitions
		return self.render_str("/definitions.html", content=text, definitions=definitions, percent=61)

class Finish(Handler):
	"""to make the last page with nearly no information on it"""
	def get(self):
		return self.render_str("/finish.html", percent=62)


# Here I instantiate the objects, creating instances of the objects of my different Classes.
t_1 = ReUse()
t_2 = OOPInfo()
t_3 = Finish()

# Here I call a function of the Class Handler, that all the other three Classes inherited from,
# thereby creating the actual HTML pages that make up my Stage 3 Project Submission.
t_1.make_page("re-use.html")
t_2.make_page("definitions.html")
t_3.make_page("finish.html")