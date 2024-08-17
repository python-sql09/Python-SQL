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





