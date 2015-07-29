### This Program is meant to generate a HTML structure with content from notes.

# -*- coding: utf-8 -*-
## (this up there I found online, it solved my issue of non-ASCII characters, but I don't know really how?)


# these two functions are the ones that actually create the string structure. note
# the ''' quotes for multi-line strings.
# this one creates the doctype declaration and the general structure, and uses
# the output of the generate_concept_html second function
def assemble_html(body_text, heading):
	start_structure = '''
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="style.css">
    <head>
    <title>
    	''' + heading + '''
    </title>
</head>
<body>
	<header>
		<h1>
			''' + heading + '''
		</h1>
	</header>'''
	end_structure = '''
</body>
</html>'''
	my_html = start_structure + body_text + end_structure
	return my_html

def generate_concept_html(title, rubric, content):
	body = '''
	<section>
    	<header>
    	    <h2>
        		''' + title + '''
   			</h2>
        </header>
    	<div>
    		<header>
    			<h3>
    				''' + rubric + '''
    			</h3>
    		</header>
    		<div>
        		<p>
            		''' + content + '''
        		</p>
        	</div>
    	</div>
	</section>'''
	return body


# these functions take out and return the heading, title, rubrics and content respectively
# from a properly formatted string
def get_heading(text):
	start = text.find('HEADING:') + 9
	end = text.find('TITLE:')
	heading = text[start : end]
	return heading

def get_title(text):
	start = text.find('TITLE:') + 6
	end = text.find('RUBRIC:')
	title = text[start : end]
	return title

def get_rubric(text):
	start = text.find('RUBRIC:') + 8
	end = text.find ('CONTENT:')
	rubric = text[start : end]
	return rubric

def get_content(text):
	start = text.find('CONTENT:') + 9
	end = text.find('TITLE:', text.find('TITLE:') + 1)
	content = text[start : end]
	return content


# get_concept_number will, given a string containing correctly formatted text
# and a number n, return the nth part of the string.
def get_concept_by_number(text, concept_number):
	count = 0
	while count != concept_number:
		count += 1
		start = text.find('TITLE:')
		if text.find('TITLE:', start + 1) != -1:
			end = text.find('TITLE:', start + 1)
			concept = text[start : end]
		else:
			concept = text[start :]
		text = text[end :]
	return concept


# this function returns a string that contains all concepts together,
# formatted in the HTML structure.
def generate_all_html(text):
    body_html = ''
    heading = get_heading(text)
    while text.find('TITLE:') != -1:
        start = text.find('TITLE:')
        end = text.find('TITLE:', start + 1)
        concept = text[start : end]
        new_concept_string = generate_concept_html(get_title(concept), get_rubric(concept), get_content(concept))
        body_html += new_concept_string
        text = text[end :]
    all_html = assemble_html(body_html, heading)
    return all_html


# opens a text file and reads its content, removing new lines.
# then it constructs a string from the data, the string is returned.
def get_text_from_file(file_name):
	my_text = open(file_name)
	my_data = ''''''
	for line in my_text:
		text_line = line.rstrip('\n')
		my_data += text_line
	return my_data



print generate_all_html(get_text_from_file('python_elements.rtf'))


## ----------- a note for the reviewer -----------

### this was a comment I had left in my code and got nicely answered with a tip
### to use JSON instead. And this is really useful! :)

### Here the original comment:
## I had problems trying to extend the automatted page creation to another level:
## I wanted to use TITLE, RUBRIC and CONTENT, with each in a different heading size,
## but didn't manage to create the iteration that would look for each rubric inside
## of one title, then make the repeating block of (rubric) html text, while keeping the
## structure otherwise correct. I will definitely try more on this. I'd have also
## an idea how to do it (I'm after all iterating through titles, which comes down
## to pretty much the same), but I can't see an easier way to do it. So I'm hoping to
## find a different way to do this, that'll be easier and more swift.
## If you have any hints for me, I'd be very glad to hear! Thanks : )


## ----------- EXTRA: -----------

# specifies the html file that gets generated
new_file = open('generated_page.html', 'w')

# uses the functions to write the raw text input as a html structure into
# the newly generated .html file.
new_file.write(generate_all_html(get_text_from_file('python_elements.rtf')))