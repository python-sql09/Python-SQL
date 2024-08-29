# Exercise 7: Last Key
# Create a script that uses the reduce() function to identify the key in a dictionary that is
# last in alphabetical order. For example, if you had the input of:
# dict_my = {"elephant":1, "zebra":4, "panther":5}
# The output would be:
# zebra
# In this case, “zebra” is the key that appears last in alphabetical order.
from functools import reduce
# Function to find the last key alphabetically in a dictionary using reduce
def find_last_key_alphabetically(input_dict):
    return reduce(lambda x, y: x if x > y else y, input_dict.keys())
# Example usage
dict_my = {"elephant": 1, "zebra": 4, "panther": 5}  # Replace with your dictionary
last_key = find_last_key_alphabetically(dict_my)
# Display the result
print("Dictionary:", dict_my)
print("Last key alphabetically:", last_key)