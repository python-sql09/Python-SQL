# Creating a string variable
name="John"
print(name)
print(type(name))

# Finding the length of a string
message = "Hello, World!"
print(len(message)) 
#prints the length (number of characters) in a string
# When you run this short listing, you see the output is simply the count of characters: 13

# Checking the length of a name
firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
print(firstname, lastname)
print(len(firstname) + len(lastname))

# Splitting a string
message = "Hello, World!"
print(message.split())

# Splitting a name
fullname = input("Please enter your full name (last name, first name): ")
print(fullname.split())

# Pulling and storing characters from a string
name = "John Smith"
print(name)
char1 = name[0] # stores the first character as char1
print(char1)
char6 = name[5] # stores the fifth character
print(char6)
char_last = name[-1] # stores the last character
print(char_last)





