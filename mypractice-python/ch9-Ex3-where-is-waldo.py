# Exercise 3: Where’s Waldo?
# Write a program to search the following tuple and find the instances of “Waldo.” Have
# your resulting program indicate how many times Waldo is found
# The given tuple
Names = ("John", "Fred", "Waldo", "Wally", "Waldorama", "Susan", 
         "Nick", "Waldo", "Waldo", "Reese", "Haythem", "Kim", "Ned", "Ron")

# Searching for "Waldo" and counting occurrences
waldo_count = Names.count("Waldo")

# Display the result to the user
print(f"'Waldo' was found {waldo_count} times in the tuple.")