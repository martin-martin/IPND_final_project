# This file contains most of the content of the auto-generated pages. I like to keep the content separated from
# the rest of the page, because like this I can keep a better overview and it is also much easier to add or
# remove content from the website.

# links mentioned in the re-use_page.html. This also represents my bibliography.
links = {"google" : "https://www.google.com",
		 "stackoverflow" : "http://stackoverflow.com/",
		 "css-tricks" : "https://css-tricks.com/",
		 "tree-structure" : "http://thecodeplayer.com/walkthrough/css3-family-tree",
		 "removing non-ASCII char" : "http://utils.paranoiaworks.org/diacriticsremover/",
		 "about some OOP definitions" : "https://alfredjava.wordpress.com/2008/07/08/class-vs-object-vs-instance/",
		 "html to embed runnable code" : "http://amasad.me/2015/04/09/hello-world/",
		 "online IDE" : "http://repl.it/",
		 "about methods": "https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods"}

# These are the definitions of the most important OOP concepts.
definitions = [['''class: ''', '''A conceptual idea that sums up certain characteristics. It is a structure that talks about which characteristics should there be for something to be part of it.'''],
			   ['''object: ''', '''The "material" representation of the blueprint of a Class. Actual houses that get built, actual forms that get filled.'''],
			   ['''instance: ''', '''An individual realization of the structure given by a Class. If a Class is a form, an instance is the form filled by someone. It's what happens to an object when it gets instantiated: <br><span><code>trip = Biking()</code></span>'''],
			   ['''method: ''', '''An in-Class-function. It is useable by all instances of that Class, but by nothing else.'''],
			   ['''module: ''', '''A python file that gets imported into another python file, thereby making its functions and Classes available for use. Requires them to be correctly called: <br><span><code>module.function()</code></span>'''],
			   ['''library: ''', '''A collection of modules. e.g. the Python Standard Library'''],
			   ['''class variables: ''', '''Variables defined inside of a Class. They are global to the Class, but not outside. Interesting e.g. for class methods.'''],
			   ['''inheritance: ''', '''Classes can inherit methods and class variables from other Classes. <br><span><code>class Biking(Travels)</code></span> <br>is the correct syntax for this. The Biking class, in this case, receives all the properties of the Travels class. It is possible to write additional methods inside of the daughter Class.'''],
			   ['''method overriding: ''', '''When one Class inherits from another Class, it is possible to override an inherited method with a different method. This happens by defining it anew with the same name in the daughter Class.'''],
			   ['''OOP: ''', '''(short for Object Oriented Programming) is a way of writing programs that focuses on the data objects rather than on the procedural logic. In OOP the challenge is to correctly describe the objects and their relationships between each other, define the kind of data they can contain and the methods that can manipulate them.''']]

# This contains the text for descriptions_page.html, it is subdivided by comments into the three main boxes.
text = {
# text for the first topic box
		'''Using (parts of) Code that's "elsewhere"''' : ['''What happens when I import a module to use in python?''',
		'''- I access another python file that contains some predefined functions.''',
		'''- I can then use these functions, by referring to them.''',
		'''<span><code>import math
math.pi</code></span>''',
		'''Yes, modules, you may say.<br>But what about Classes?''',
		'''<hr>''',
		'''In some ways they behave like an in-file-module. As if I would create another python file within my python file, when I define a Class. How do I mean this? The Class contains methods (in-Class functions), and I can call these methods with the same syntax as calling a function from a module:''',
		'''<span><code>module_name.function()
ClassName.method()</code></span>''',
		'''Given, I have to first create a Class, its methods, and instantiate a Class object:''',
		'''<span><code>class Biking:
	def __init__(self, start_date, end_date):
		self.start_date = start_date
		self.end_date = end_date
	def get_days(self):
		self.days = self.end_date - self.start_date
		return self.days</code></span>''',
		'''If I have now also created an instance of the Class Biking, say <span><code>trip = Biking(6, 9)</code></span> then I can call the method on it:''',
		'''<span><code>Biking.get_days(trip)</code></span>''',
		'''where I pass the instance I created before as the first (and here only) argument to the function call, the others arguments I need for it to work have already been passed while creating the instance and are saved in there. Therefore when passing that instance, I automatically also have the associated variables available. This is possible because of the "self." prefix. If the method would require additional arguments, they would be passed here after the instance just as in a normal function call.''',
		'''Another way to call Class methods on an instance of that Class, making the syntax maybe in some ways a bit easier, is:''',
		'''<span><code>trip.get_days()</code></span>''',
		'''This is also the standard way of calling a method on a Class object. However it might shade a bit the relationship between modules and Classes, so this is why I wanted to write about the other way (first).''',
		'''Methods are essentially a part of their Class, and in a way they make up the structure in which the data objects reside. If I create a Class it's as if I'd make a space with certain rules (methods) in which certain beings (objects) can exist and interact. Methods also define how my Class objects can communicate with the outside world.''',
		'''<hr>''',
		'''Another interesting thing I learned from my second review, is that there are different kinds of methods. One I had defined in an earlier version of my page would actually be more properly described like this:''',
		'''<span><code>@staticmethod
def distance(a, b):
	path_km = b - a
	return path_km</code></span>''',
		'''It is a so called "static method", because it doesn't actually need nor handle the Class object at all. The advantage of defining such a method without a "self." prefix is, that when inheriting methods to a child Class, we don't need to override other methods of the parent Class that are using the static method, if we only want to change that specific static method. It also brings performance improvements, but this I am not yet versed enough to know how to consider  :)''',
		'''There's a bunch of other special methods, and <a href="https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods">this here</a> is a page with good descriptions of them!'''],
# text for the second topic box
		'''Class/Instance-relationships outside programming''' : ['''Generally, the relationship between a Class and an instance of the Class, is the same as in taxonomy.''',
		'''This and that animal are part of one together species.<br>The species description sums up certain points that the two individuals have in common: "general" aspects. In the analogy: the individuals are instances of the Species Class.''',
		'''<hr>''',
		'''<strong>Tasks:</strong>''',
		'''- Make some mini-taxonomy, some animals or some plants, to describe visually Classes and Objects. <a href="rodents.html">(linked here!)</a><br>''',
		'''- Use Class concepts in generating this HTML page. (look into compile.py)''',
		'''- Import a python online environment into the website so the Class example code can be run (<a href="#codetry">see section below</a>)'''],
# text for the third topic box
		'''Using Classes: An Example''' : ['''Now the point of having Classes is exactly this: that all the Objects that are part of the same Class share the same "characteristics". In the case of programming, this means that they share the same methods. And therefore, stuff can be done with them in the same way.''',
		'''We could e.g. create a Class called Food, then create two objects:''',
		'''<span><code>carrots = Food()
tomatoes = Food()</code></span>''',
		'''and we could define the method''',
		'''<span><code>eat(self)</code></span>''',
		'''inside this Class.''',
		'''We would then be able to apply the method eat() to both instances of our Food Class and we wouldn't have to go hungry tonight''',
		'''Imagine that in our outdoor excitement program we also have the variable stone, maybe it was assigned like this:''',
		'''<span><code>stone = "hard"</code></span>''',
		'''Now if we'd take a peek at all the variables that exist in our surroundings, we would say "aha, there's carrots, tomatoes and stone"''',
		'''They might even look quite the same considered in this way! (for the reality transfer, imagine that it's either quite a crappy tomato or a pretty red stone.)''',
		'''Since stone is, however, not an Object of the Food Class, this:''',
		'''<span><code>stone.eat()</code></span>''',
		'''would throw an error.''',
		'''while this works sweetly fine and fills the stomach:''',
		'''<span><code>tomatoes.eat()
carrots.eat()</code></span>''',
		'''There you go. Classes in a nutshell.''',
		'''<span><code>nutshell = 2
nut = Food()
nut.eat()</code></span>''',
		'''njam.''']}
