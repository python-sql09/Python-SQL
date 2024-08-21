# Exercise 2: Modifying Tuples
# Starting with the combined tuple from the previous exercise
combined_tuple = ('John', 'Doe', 'Software Engineer', '123 Main St', 'New York, NY', '10001', '456 Elm St', 'Boston, MA', '02118')

# Display the tuple to the user
print("Current tuple:")
print(combined_tuple)

# Convert the tuple to a list to allow modifications
combined_list = list(combined_tuple)

# Ask the user for the value they want to change
value_to_change = input("Enter the value you want to change: ")

# Check if the value exists in the list
if value_to_change in combined_list:
    # Get the index of the value
    index = combined_list.index(value_to_change)
    
    # Prompt the user for the updated value
    updated_value = input("Enter the updated value: ")
    
    # Update the value in the list
    combined_list[index] = updated_value
    
    # Convert the list back to a tuple
    updated_tuple = tuple(combined_list)
    
    # Display the updated tuple to the user
    print("Updated tuple:")
    print(updated_tuple)
else:
    print("The value you want to change is not in the tuple.")