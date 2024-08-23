# Exercise 3: Finding the Largest
# Define the find_largest function used in the following code snippet. The function should
# compute the largest value from an input list of numbers and print the result:
# Put your function code here
def find_largest(numbers):
    # Use the built-in max() function to find the largest number in the list
    largest = max(numbers)
    # Print the largest number
    print(f"The largest transaction amount is: {largest}")
# do not change this code below
transactions = [1000,55322,511000,700,1050,1200]
find_largest(transactions)