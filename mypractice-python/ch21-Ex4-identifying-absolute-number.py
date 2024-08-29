# Exercise 4: Identifying Absolute Value
# Create a script that uses the map() function to compute the absolute value of each integer
# in an input list.
# Function to compute the absolute value of integers in a list using map
def compute_absolute_values(input_list):
    return list(map(abs, input_list))

# Example usage
input_values = [-5, 3, -2, 7, -10, 0, 15]  # Replace with your list of integers
absolute_values = compute_absolute_values(input_values)

# Display the results
print("Original values:", input_values)
print("Absolute values:", absolute_values)