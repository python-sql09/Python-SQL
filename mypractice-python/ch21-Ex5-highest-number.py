# Exercise 5: Highest Number
# Create a script that uses the reduce() function to compute the highest number in a tuple.
from functools import reduce
# Function to compute the highest number in a tuple using reduce
def find_highest_number(input_tuple):
    return reduce(lambda x, y: x if x > y else y, input_tuple)
# Example usage
input_tuple = (3, 7, 2, 8, 5, 10, 1)  # Replace with your tuple of integers
highest_number = find_highest_number(input_tuple)
# Display the result
print("Input tuple:", input_tuple)
print("Highest number:", highest_number)