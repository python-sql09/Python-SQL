# Exercise 6: Lowest Number
# Create a script that uses the reduce() function to compute the lowest number in a tuple.
from functools import reduce
# Function to compute the lowest number in a tuple using reduce
def find_lowest_number(input_tuple):
    return reduce(lambda x, y: x if x < y else y, input_tuple)
# Example usage
input_tuple = (3, 7, 2, 8, 5, 10, 1)  # Replace with your tuple of integers
lowest_number = find_lowest_number(input_tuple)
# Display the result
print("Input tuple:", input_tuple)
print("Lowest number:", lowest_number)