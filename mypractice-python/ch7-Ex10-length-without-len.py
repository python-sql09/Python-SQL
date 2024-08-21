# Ask the user for a string
user_string = input("Enter a string: ")

# Compute the length of the string without using len()
length = 0
for _ in user_string:
    length += 1

# Display the length of the string
print("The length of the string is:", length)