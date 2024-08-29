# Exercise 9: Sum of Even
# Create a script that uses the reduce() function to compute the sum of all even numbers
# in a list of numbers. For example, given the list [3, 4, 5, 9, 6], the output should be 10
# (because 4 and 6 are the only even numbers in the list, and 4 + 6 = 10).
from functools import reduce
# Function to compute the sum of even numbers in a list using reduce
def sum_of_even_numbers(numbers):
    return reduce(lambda acc, num: acc + num if num % 2 == 0 else acc, numbers, 0)
# Example usage
numbers = [3, 4, 5, 9, 6]  # Replace with your list of numbers
sum_even = sum_of_even_numbers(numbers)
# Display the result
print("List of numbers:", numbers)
print("Sum of even numbers:", sum_even)