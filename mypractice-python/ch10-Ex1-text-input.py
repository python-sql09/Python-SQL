# Exercise 1: Working with Text
# Write a program that inputs a text file. The program should print the unique words in the
# file in the form of a dictionary in alphabetical order.
import string

# Get the filename from the user
filename = input("Enter the filename (with extension): ")

# Create an empty dictionary to store unique words
word_dict = {}

# Open the file in read mode
file = open(filename, 'r')

# Read each line in the file
for line in file:
    # Remove punctuation and convert to lowercase
    words = line.translate(str.maketrans('', '', string.punctuation)).lower().split()
    
    # Add each word to the dictionary
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1  # Add word to the dictionary

# Close the file after reading
file.close()

# Sort the dictionary by the keys (words)
sorted_words = dict(sorted(word_dict.items()))

# Print the sorted dictionary
for word in sorted_words:
    print(word)