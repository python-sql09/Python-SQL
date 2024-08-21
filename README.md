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
•• User-­defined functions are functions defined by the user. These functions use the
def keyword to define them.
•• Built-­in functions are functions that are built into Python.
•• Redundancy checking is used to check that the same code lines are not unneces-
sarily repeated within an application.
•• Docstrings (short for Python documentation) are used to organize functions, mod-
ules, classes, and methods. Docstrings are similar to comments, but docstrings
describe what the function does rather than how.
•• Parameters are the variables listed inside the parentheses in the function defini-
tion. You can think of parameters as variables that we define as part of defining a
function. Their purpose is to store the values provided by our function arguments.
•• Arguments are pieces of information passed into functions. An argument is the
value sent to the function when called upon.

DEFINING FUNCTIONS IN PYTHON
As we stated earlier, a function in Python is a block of organized, reusable code. A function performs a single, related action. A function in Python can take any number of parameters. When defining functions within Python, we must adhere to the following rules:
•• Python function blocks begin with the keyword def followed by the function name
and parentheses ().
•• Input arguments should be placed within these parentheses.
•• The first statement of a function can be an optional statement—­the documentation
string of the function, or docstring.
•• We exit a function using the statement return [expression]. The exit function
may optionally pass back an expression to the caller of the function. The action of
Return None would essentially provide an indication that the function completed
successfully, while no return function leaves the function to operate with no return
as if it was completed.
•• The colon (:) delineates the start of the function code block, which should
be indented.

def function_name(function_parameters):
function_body # Set of Python statements
return # optional return statement






