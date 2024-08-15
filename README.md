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