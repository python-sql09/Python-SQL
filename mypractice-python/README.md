# Python
Table 8.1  Types of Data Structures
---------------------------------------------------------------------------------------
Structure 		        Syntax 				            Definition
----------------------------------------------------------------------------------------
List 		Lists are enclosed in brackets:		   Lists are ordered and changeable.
		    l = [1, 2, "a"]
Tuple 		Tuples are enclosed in parentheses:	   A tuple is ordered and is immutable 
		    t = (1, 2, "a")				            (cannot bechanged).
Dictionary 	Dictionaries are built with		      A dictionary is unordered, changeable,
		    curly brackets:				          and indexed. Dictionaries have keys
		    d = {"a":1, "b":2}			            and values.
 Set 		Sets are written with curly		        A set is an unordered collection
		    brackets:				              of items. Every set element is unique 
		    s = {1, 2, 3}				           and must be immutable (cannot be     
                                                    changed). However, a set itself ismutable. We can add or remove items from it.
----------------------------------------------------------------------------------------


Table 8.3 Comparison of the ways for removing items from a list
----------------------------------------------------------------------------------------
remove()					pop()						del
----------------------------------------------------------------------------------------
Method					Method						Keyword
Uses a value			Uses an index				Uses an index
Single item removed		Single item removed	S		ingle item or entire list removed
No return value			Removed value returned		No return value
----------------------------------------------------------------------------------------
Tuple:
-----
A tuple is another way to save a group of related pieces of data in Python. The biggest
difference between a tuple and a list is that a tuple is immutable, which means that we cannot add or remove items from a tuple after we have defined it.

Slicing Tuple
-------------
•• tuple[x:y]: Retrieves a range of values starting with index x and ending with the
item before index y. If y is equal to the length of the list, the output includes the
last item in the list.
•• tuple[:y]: Retrieves the items from index 0 through the item before index y. This
is equivalent to using [0:y].
•• tuple[x:]: Retrieves a string that starts with the item whose index is x and includes
all items to the right of that character. This is equivalent to using [x:(length)]


Method						Description

keys()				Returns a list containing the dictionary’s keys
items()				Returns a list containing a tuple for each key: value pair
values()			Returns a list of all the values in the dictionary
get()				Returns the value of the specified key
pop()				Removes the element with the specified key
update()			Updates the dictionary with the specified key: value pairs
copy()				Returns a copy of the dictionary
clear()				Removes all the elements from the dictionary


GETTING STARTED WITH DICTIONARIES
A dictionary is a collection of items using defined keys. The key acts as a unique index,
which does not have to be an integer, and each key maps to a specific value in the dic-
tionary. Each item in a dictionary is a pair made of a key and a value. Dictionaries are not
sorted. Dictionaries are written with curly braces {}.

MyFirstDict = {
"key1": "value1",
"key2": "value2",
"key3": "value3"
}

Table 10.2 Common Dictionary Methods
-----------------------------------------------------------------------------------
Method                                     Description
-----------------------------------------------------------------------------------
keys()			Returns a list containing the dictionary’s keys
items()			Returns a list containing a tuple for each key: value pair
values()		Returns a list of all the values in the dictionary
get()			Returns the value of the specified key
pop()			Removes the element with the specified key
update()		Updates the dictionary with the specified key: value pairs
copy()			Returns a copy of the dictionary
clear()			Removes all the elements from the dictionary
-----------------------------------------------------------------------------------

FUNCTIONS OVERVIEW
-------------------
A function is a block of organized, reusable code that uses one or more Python state-
ments to complete a single, related action. We use functions to help with code reusability, increased readability, and redundancy checking (making sure that we do not use the same lines over and over within an application).

•• Functions are blocks of organized, reusable code.
•• Function code blocks are groups of Python program code executed as a unit, such
as a module, a class definition, or a function body. A colon (:) is used to start a
function code block.
•• User-­defined functions are functions defined by the user. These functions use the def keyword to define them.
•• Built-­in functions are functions that are built into Python.
•• Redundancy checking is used to check that the same code lines are not unnecessarily repeated within an application.
•• Docstrings (short for Python documentation) are used to organize functions, modules, classes, and methods. Docstrings are similar to comments, but docstrings
describe what the function does rather than how.
•• Parameters are the variables listed inside the parentheses in the function definition. You can think of parameters as variables that we define as part of defining a function. Their purpose is to store the values provided by our function arguments.
•• Arguments are pieces of information passed into functions. An argument is the value sent to the function when called upon.

DEFINING FUNCTIONS IN PYTHON
As we stated earlier, a function in Python is a block of organized, reusable code. A function performs a single, related action. A function in Python can take any number of parameters. When defining functions within Python, we must adhere to the following rules:
•• Python function blocks begin with the keyword def followed by the function name and parentheses ().
•• Input arguments should be placed within these parentheses.
•• The first statement of a function can be an optional statement—­the documentation
string of the function, or docstring.
•• We exit a function using the statement return [expression]. The exit function may optionally pass back an expression to the caller of the function. The action of Return None would essentially provide an indication that the function completed successfully, while no return function leaves the function to operate with no return as if it was completed.
•• The colon (:) delineates the start of the function code block, which should be indented.

def function_name(function_parameters):
function_body # Set of Python statements
return # optional return statement

OBJECT-­O RIENTED PROGRAMMING OVERVIEW
---------------------------------------
Object-­oriented programming (OOP) is a programming paradigm based on objects.
There are four principles that define and differentiate object-­oriented programming. These principles are encapsulation, abstraction, polymorphism, and inheritance.

•• Classes are a type of object with a state and behavior. (Example: the vehicle class)
•• Objects is an instance of a class. (Examples: Honda Accord, Toyota Camry, midsize
vehicle, luxury vehicle)
•• Attributes define a property of an object. (Example: vehicles have four wheels)
•• Encapsulation is the formation of a digital barrier around a class that keeps the
information hidden from the rest of the code in the program.
•• Abstraction is an extension of encapsulation; abstraction keeps object-­oriented
programming simple in that certain properties and methods from the outside code
are hidden.
•• Polymorphism is the ability of an object within the object-­oriented programming
paradigm to take on many forms.
•• Instantiation is the process of allocating memory for an object after its constructor
has been run.
•• Constructors are a unique method that Python calls for instantiations (creations) of
object definitions found within a class.

DEFINING CLASSES
----------------
When using an object-­oriented approach to software development, classes represent or describe real-­world entities. To define a class, we use the keyword class followed by the name of the class. Within the class, we define its attributes, which describe its state.
class VehicleClass:
	pass

class Person:
	# init method or constructor
	def _ _init_ _(self, name):
	self.name = name #name is an instance attribute.


•• Inheritance allows the definition of classes to inherit methods and properties from
other classes.
•• Parent class or base class is the original class that is being inherited from. This can
be any standard class.
•• Child class or derived class is a class that inherits the functionality of the
parent class.

Creating a Variable for a Date
--------------------------------
•• Python’s datetime module supplies classes for manipulating dates and times.
•• The now() function is used to display the current date and time.
•• The today() function returns the current local date and time.

datetime.date(year, month, day)
user_date = datetime.date(int(year),int(month),int(day))

Creating a Variable for Time
----------------------------
datetime.time(hour, minute, second)

Creating a Variable for Both Date and Time
-------------------------------------------
In addition to the date() and time() methods, there is a datetime() method within the datetime class that works with both at the same time.
datetime( year, month, day, hour, minutes, second)

GETTING THE CURRENT DATE AND TIME
---------------------------------
We can use the attributes now() or today() to reference the current system
time and date:
•• now() always includes both date and time.
•• today() always includes date, but time is optional.

SPLITTING A DATE STRING:
-------------------------
We can use string functions to extract individual pieces of a datetime output.

USING DATETIME ATTRIBUTES
-------------------------
Although we just saw how to split a datetime string into its various components, there is an easier way to get the pieces. The datetime module has several attributes built i­n:
•• year
•• month
•• day
•• hour
•• minute
•• second
•• microsecond
•• time zone information (tzinfo)

APPLYING TIMESTAMPS
--------------------
value = datetime.datetime.timestamp(some_date)

FILE PROCESSING OVERVIEW
------------------------
•• Size constraints are lifted
•• Data can be input more quickly
•• Data can be used with different applications

• Path: A path identifies the location of the file to be utilized. A path can be absolute or relative.
•• Absolute path: A path that includes all information required to find the file, regardless of where the script is stored.
•• An absolute path starts with a forward slash in front of a topmost folder and includes all subfolders leading to the target file, such as /Users/username/Documents/Python Scripts/fileio/data/testfile.txt.
•• Absolute paths are useful if the Python scripts are not stored in the same parent folder as the target files, or if the Python scripts may be used in different places in a system.
•• Relative path: A path that starts from the directory where the Python script is stored and includes instructions on how to get to the file using that directory as a starting point.
•• Building on the example of an absolute path, if the Python script file is stored in the fileio subdirectory, the relative address to the same file is data/testfile.txt.
•• Relative paths are shorter, but they depend on the location of the Python script to work. If the files and scripts are stored independently of each other or if the script file may be moved to a different directory at a later time, an absolute path may be a better option.

INTRODUCTION TO FILE INPUT/OUTPUT
----------------------------------
Python documentation (https://docs.python.org/3/tutorial/inputoutput.html) for all functions available. The basic functions and methods listed here are:
•• input()
•• open()
•• read()
•• write()
•• close()
•• print()

The input() Function
---------------------
Python uses the input() function to read data from standard input, which by default comes from the keyboard.
input(prompt)

The open() Function
--------------------
Before we can read or write a file, we must open it. We open it using Python’s built-­in open() function. This is the main function for working with files in Python. The open() function takes two parameters: filename and mode.

The read() Method
------------------
The read() method reads a string from an open file. It is important to note that Python strings can have binary data apart from text data. The basic syntax of the read() method is:
fileObject.read([count]);

The write() Method
-------------------
The write() method writes any string to an open file. It is important to note that Python strings can have binary data and not just text. The write() method does not add a newline character (\n) to the end of the string. The basic syntax of the write() method is:
fileObject.write(string);

The close() Method
-------------------
The close() method of a file object flushes any unwritten information and closes the file object, after which no more writing can be done. The basic syntax of the close() method is:
fileObject.close();

The print() Function
--------------------
The simplest way to produce output is by using the print() function, which we’ve used throughout this book. Using the print() function, you pass 0 or other expressions separated by commas. The basic syntax of the print() function is:
print ("12345")

OPENING A FILE
---------------
open("path to the file","r,a,w,x")

•• r: Open the file as read-­only. Python throws an error if the file does not exist.
•• a: Open the file for appending. The original content cannot be changed, but we can add new content to the file. If the file does not yet exist, Python will create it.
•• w: Open the file with full editing options, including changing existing content or adding new content. Python will create the file if it does not already exist.
•• x: Create a new file with the specified name. Python returns an error if a file with that name already exists.

To open a file for input, use "r". If a file with the same name is not accessible, Python raises an error. The code for opening thefile.txt for input is:
f = open ("thefile.txt", "r")
A script that opens a file should close the file as well, to remove the file from memory and free up resources:
f.close()

