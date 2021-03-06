READ THIS FILE IF YOU ARE INTERESTED IN SOME MORE INFORMATION ABOUT MY THOUGHTS AND MY PROCESS WHILE DOING THE INDIVIDUAL STAGES AND THIS FINAL PROJECT. 

IT CONTAINS SOME  INFORMATION AND EXPLANATIONS ABOUT WHAT I WAS DOING IN THESE PROJECTS AND MIGHT ANSWER ONE OR TWO POSSIBLE QUESTIONS (AND MAYBE RAISE SOME OHTERS).
: )

____

BASIC STRUCTURE OF MY FINAL PROJECT:
-----
This is a stich-job.

During the IPND I went a long way from knowing basically nothing about making webpages, up to reaching a certain level, where I started to include JS.
I treated all the Projects as individual Projects, starting anew each time and focusing on different aspects, related to what I was interested in from the inputs I got from the respective stages.

It was difficult to bring them together onto an online website.

I had to change some things, include some new, exclude some old functionality. I worked like with a needle, doing small things that needed focus and were sometimes difficult to see. I needed to create a string, and then sew it through the fabric of my scattered project pages.
There are some flapping bits that maybe didn't find their place completely naturally in the new clothes I made. Some extras (that might even not be visible except when you go to investigate the sketches on my github), and some cut-offs.

But all together I am quite satisfied with what I created. It looks good to me, and it tells my story a bit. :D

If you want to take a look and read the stories that my code tells, I welcome you to my new robe that is in itself a story of how I learned to code.



**My final project contains the following resources:**

**/css**
this folder contains all the CSS files that are used for the online version of the page on appspot

**/data**
here lie the files that provide the data for the pages, as far as it was stored outside of the HTML templates.

**/data/REVIEW_NOTES**
contains three txt files with my communication with the reviewers of my later stages. I was often dissatisfied with the reviews. I received, but felt like giving a useful feedback to my reviewers, so I started to create and append this document, that would clarify to the (new) reviewer what happened before, what I said and what I changed.

**/data/stage2_auto**
just as /stage_auto this contains my original submission for these two stages. They both were composed (partly) of auto-generated pages and I wanted to include the whole functionality in my project repository. If you want to see these pages getting made, you can download these folders and run the files html_generator.py and compile.py respectively.

**/data/pages_tems.json**
This file contains a very important part of my final
project - I use its data to create multiple pages with one handler using regex. This was something I learned while doing this final project, after all Stages were already submitted and graded.
But it was a very interesting point to learn about, and I'm happy I got it to work, even though my regex knowledge is still only tiny.

**/data/s3_content.json** and
**/data/s5_about_js.json**
both files contain data for the respective pages in JSON format

**/data/s4_notes_stage_4.text**
this file was added to my stage 4 submission, because due to the nature of my stage 4 project, my notes were entered into the form page I created, and therefore not completely obvious. I included this file as a prove that the first submission was indeed mine.

**/font**
contains the one special font that I used for my stage 2 project. It is a font that is similar to the official python font. Mainly it was interesting to learn about the fact that some fonts need to be added if I'll want my page to also display them, and that otherwise there are browser standards that the (missing) font gets replaced by.

**/img**
in this folder are all the images that I use for the respective stages. There is also one additional image, a favicon that I created now while doing the final project putting all stages together. I made it myself with one online tool, and I find it quite cute actually :)

**/js**
in here are the (so far) only .JS files that I am using for this project. I created it while working on Stage 5, and I am also using it for the functionality of the landing page. It's not a lot of JS, but I worked on it for quite a while, trying to learn and understand things about this new language. Knowing a bit of python helped a lot, but I'm only a very beginner in all this.

**/templates**
this folder contains all the HTML templates that get rendered for my appspot final IPND page. They are sorted in stages, with some files also just directly in the parent directory, if they don't belong to a specific stage but more the final project.

**/templates/links_tem.html**
is a file that I am currently not yet using, which would in the end contain some kind of bibliography of the links that I used and learned from. I haven't yet made it, also because I am not completely sure as of how I'd want it to be.

**/app.yaml**
the .yaml file for my project. I'm happy to have gotten my URL :)

**/compile.py**
this is the python file that does all the compiling, basically the heart of the project. It assigns the handlers and calls appengines services, classes and methods, and here I do a lot of the stitching together.

**/README.md**
the short description for the github page.

**/INFO.txt** and **/INFO.md**
And finally: this file itself. Probably best described as a mix of a README and a reflective diary entry. :) There's two versions because I was trying to make it better readable through using markdown, but I also kept the original file around.


----

ABOUT MY PROJECTS
----

**STAGE 0:**

After having previously played a bit on some online platforms, this was the first time I actually sat down to code a webpage. It was quite exciting to see things come together, especially proud I was at the orange frames around my tag symbol examples. :)

Wanting to talk about tags on the page, I was right away confronted with HTML escaping, even though I didn't know what this was then.
Found the solution online to use &lt notation (I then didn't know about the ";" to close it off, Sublime marked it pink for me and I found this sweet, not realizing then that it meant that there's a mistake...).

**STAGE 1:**

I went to fix some of the mistakes from my Stage 0 submission. I didn't include that webpage again in this collection, because it is quite the same as Stage 0, and therfore a bit boring to look at. In Stage 1 I learned about the "Inspect Element" feature in Chrome. This opened quite a world since I started to understand that this way it becomes possible to look into the source code of every website. Which means that there is an extremely rich resource to learn about how to do things, simply by checking how was something done, that seems to be good.

Here in this Stage I think I learned a lot about using CSS, and I invested my time into trying to get some things to look in a way that I wanted it to look like. I included a little mini-riddle, that you are welcome to think about: What's the rule according to which some words get an orange highlighting? : ) it's very easy, but I felt cute about making it.
I also used the outline in CSS quite a bit and I believe this was very useful to help me fortify my understanding how content is put in boxes in HTML.
Since I was trying around a bit with styles, these pages are a little redundant in terms of my content in notes.

**STAGE 2:**

This stage marked for me a big step in my development. I learned to auto-generate a page from a text file (the first page when entering Stage 2). It was a messy job from my current perspective, but I didn't know many things then... :) I read my input from a .rtf file and needed to refer to an online tool to rid my text of non-ASCII characters, and even ended up using some code "magic" I found around that finally made it work out. Messy. : ) But I was quite proud on managing to achieve this task!

In my github repository I therefore left also the folder that contains my python code and the source text file that work together to auto-create this webpage, and if you're ready for some young try-arounds, you can go and take a look at it (data/stage2_auto).

The second thing that remained in my memory for this stage was, that I spent a lot of time tweaking the style of the page, researching on the web for fitting fonts and colours, to make them "python original", for images that would fit, and all in all I maybe spent the most time on styling of all pages that I did for the IPND. I think I reached a certain point with working on this submission stylewise, understanding that there is quite a lot that I can already do if I want to - but also that tweaking is often very time-intensive and that it's only worth to do this if I really want to achieve a certain look. Often for the later stages I chose to use much simpler CSS, since I was focusing much more on the functionality and the new learnings. But knowing that I can make a page look good (according to my standards) was quite an important learning.

Another thing that I did here, was that I made little detours and small jokes built into my website. I set little "traps" for the visitor, throwing them into loops they would have to walk in case they clicked some link on the pages. I think it is mostly a little blink with the eye ;) - but maybe also speaks of a point that often there's a lot to click on the web, and it doesn't necessarily bring you to the most useful places.

**STAGE 3:**

I chose to also auto-generate the pages for this project, since I was discontent with the videos of this stage. I wanted to understand more about OOP, and do more practical exercises than only write my notes. Therfore I ditched the rubric and went on a coding walk. :)
There's a question about how to better store the content, since I wasn't happy with the .py file way of doing it, and I got (again) pointed into the direction of JSON. I grew to really like JSON for its simplicity, as a solution to storing content elswhere. Because this I really like.
Again, as in Stage 2, I left the whole project folder on my github repository for this project (data/stage3_auto), so that it is still possible to view the functionality of auto-generating those pages how they originally did.
So, for this new version of my Stage 3, I refactored my data into a JSON file, and the code for the online webpages on appspot now draw their data from that source. :)
In this stage I used knowledge from Stage 4 to work with jinja2 and HTML templates. This concept was very exciting for me and I learned a lot about how the web is made through it. Suddenly, some things made sense :)
I also searched for and used some code from other sources, in order to practice a bit how to include bits of code that others wrote into my project. I guess also in this lies quite a lot of truth about how the web is made!
My notes revolve around some abstractions about what Object Oriented Programming is, as I was trying to teach myself a little more about the how and what of it all.

**STAGE 4:**

If I had to choose one, I guess this would be my choice for my favourite stage. The instructor was very nice, funny, and competent. I learned a lot of new stuff and got some things to work that I never did before. There was an introduction to databases, Handlers were written, and something dawned about the nature of webapps and therfore another big piece of how is the internet doing these days.
I was very excited about doing this project, also because I definitely wanted to create all this functionality that he was talking about in the lectures. During a test, I had created a page filled with all the different forms that we had learned earlier for a friend, and maybe it was part of inspiring me to create my stage 4 project in a way, that it would be about itself (as everything is in this course), yet still interactive.

I went to make it a possibility for other students to share their experience and thoughts, and I'm excited that this page might be online for a while and maybe some people will actually be writing some cute or interesting things on there.

I played again a bit with styles, but mainly through the aspect of forms and options, I used again HTML templates, and I also got to know how to operate google app engine a bit and how to deploy a website and make it actually float up there in the vastness of the net.

One thing I also did, was that I went to revisit again some of the many many emoticons that exist out there : )

**STAGE 5:**

I haggled with Javascript. There were many other very interesting topics in this stage. It was beautiful to watch this person creating the word game, but I feel still very far from understanding anything such in depth. Maybe this part is a good grounder after one starts feeling that, wow, I already know a bit how to program... (there's much much more out there!)
Well, for this project I wanted to make a progress bar, because I am often missing graphical (or any) kind of feedback for the things I am doing, so being able to create myself progress bars for whatever I'd want to, feels like a useful thing for me to learn to do well.


--------

Text for the forum post
---
Hei everyone!

I've finished my IPND! :D

So I took some time to do my Stage 6 ;), which means I stuck all my different projects together to create one big IPND website, that I've put up on appspot here: 

http://ipnd-all.appspot.com/

It was a good thing for me to do because it made me revisit all the Stages a little bit, refresh some knowledge, and handle some new problems coming from the fact that these things were not originally made to be put together...

I learned new things, but I wanna know more!
So if you feel like taking a look at some or all of my IPND projects put on one pile, I hereby warmly welcome you for a visit.

You can either take a graphical walk here or dive right into the code here on my github.

I'd be very glad to receive tips and comments, so if there's something you know how to improve or if you discover something that doesn't work, or just have an idea what might be a cool thing to do, I'd be glad if you'd write me some feedback!

Digging through my code again I also unearthed some yet unanswered questions that I'll post here. Some I answered now on the way, some I'm hoping to get some good tips :) Maybe this can give a direction of what to look for (because I know that all these projects at once is probably a bit too big a piece to swallow).

---------


Thanks for any input, and I hope you'll maybe have a nice time looking through my pages or my code!

And good luck for your own projects! :)
