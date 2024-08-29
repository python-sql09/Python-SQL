# Exercise 8: Highest Value
# Create a script that uses the reduce() function to identify the highest value in a diction-
# ary. For example, if the input was:
# dict_my = {"elephant":1, "zebra":4, "panther":5}
# Then the output would be:
# panther
# In this case, “panther” has the highest value, 5.
from functools import reduce
# Function to find the key with the highest value in a dictionary using reduce
def find_key_with_highest_value(input_dict):
    return reduce(lambda x, y: x if input_dict[x] > input_dict[y] else y, input_dict)
# Example usage
dict_my = {"elephant": 1, "zebra": 4, "panther": 5}  # Replace with your dictionary
key_highest_value = find_key_with_highest_value(dict_my)
# Display the result
print("Dictionary:", dict_my)
print("Key with the highest value:", key_highest_value)