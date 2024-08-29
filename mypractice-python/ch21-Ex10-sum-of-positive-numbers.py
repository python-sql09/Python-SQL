# Exercise 10: Sum of Positive Numbers
# Create a script that uses the reduce() function to compute the sum of all positive num-
# bers within a list of numbers. For example, the input [1, 2, -­1, -2, 1] should output 4
# (1 + 2 + 1).
from functools import reduce
# Function to compute the sum of positive numbers in a list using reduce
def sum_of_positive_numbers(numbers):
    return reduce(lambda acc, num: acc + num if num > 0 else acc, numbers, 0)
# Example usage
numbers = [1, 2, -1, -2, 1]  # Replace with your list of numbers
sum_positive = sum_of_positive_numbers(numbers)
# Display the result
print("List of numbers:", numbers)
print("Sum of positive numbers:", sum_positive)