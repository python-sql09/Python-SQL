# Exercise 1: Computing the Square Root
# Create a script that uses the map() function to compute the square root of each value in
# an input set of integers.
import math

# Function to compute the square root
def compute_square_root(values):
    return list(map(math.sqrt, values))

# Example usage
input_values = {4, 16, 25, 36, 49}  # This is a set of integers
square_roots = compute_square_root(input_values)

# Display the results
print("Original values:", input_values)
print("Square roots:", square_roots)