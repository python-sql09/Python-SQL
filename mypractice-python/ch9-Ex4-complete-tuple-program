# Exercise 4: A Complete Tuple Program
# Create a tuple with at least five elements
original_tuple = ("Apple", "Banana", "Carrot", "Doughnut", "Egg")
updated_tuple = original_tuple

# Ask for the user's first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

while True:
    # Display the current tuple
    print("\nCurrent tuple:", updated_tuple)    
    # Ask for a value
    value = input("Enter a value: ")

    # Ask for an operation ("add" or "remove")
    operation = input("Would you like to add or remove the value? (type 'add' or 'remove'): ").lower()

    # Convert tuple to a list for modification
    updated_list = list(updated_tuple)

    if operation == "remove":
        if value in updated_list:
            # Remove the value if it exists in the list
            updated_list.remove(value)
            updated_tuple = tuple(updated_list)  # Convert back to tuple
            print("Updated tuple after removal:", updated_tuple)
        else:
            print("Error: The value does not exist in the tuple.")

    elif operation == "add":
        if value in updated_list:
            print("Error: The value already exists in the tuple.")
        else:
            # Add the value to the list if it does not exist
            updated_list.append(value)
            updated_tuple = tuple(updated_list)  # Convert back to tuple
            print("Updated tuple after addition:", updated_tuple)

    else:
        print("Invalid operation. Please type 'add' or 'remove'.")

    # Check if the user wants to quit
    quit_program = input("Type 'quit' to exit or press Enter to continue: ").lower()
    if quit_program == "quit":
        break

# Display final results
print("\nOriginal tuple:", original_tuple)
print("Final tuple:", updated_tuple)

# Calculate the difference between original and updated tuples
original_set = set(original_tuple)
updated_set = set(updated_tuple)
difference = updated_set - original_set

print("Difference between original and final tuples:", difference)
print("Your name:", first_name + " " + last_name)