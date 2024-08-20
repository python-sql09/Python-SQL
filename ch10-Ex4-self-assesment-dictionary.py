# Exercise 4: Self-­Assessment
# Original dictionary with five elements
original_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'job': 'Engineer',
    'hobby': 'Photography'
}

# Create a copy of the original dictionary for modification
updated_dict = original_dict.copy()

print("Welcome to the dictionary program! Type 'quit' to exit.")

while True:
    # Ask the user for a key
    key = input("Enter a key: ")
    
    # Exit the loop if the user types 'quit'
    if key.lower() == "quit":
        break
    
    # If the key exists in the dictionary
    if key in updated_dict:
        print(f"The key '{key}' already exists with value '{updated_dict[key]}'")
        operation = input("Do you want to 'update' or 'remove' this key? ").lower()
        
        if operation == "remove":
            # Remove the key-value pair from the dictionary
            del updated_dict[key]
            print(f"Key '{key}' has been removed.")
        
        elif operation == "update":
            # Ask for a new value and update the dictionary
            new_value = input(f"Enter the new value for key '{key}': ")
            updated_dict[key] = new_value
            print(f"Key '{key}' has been updated with value '{new_value}'")
        
        else:
            print("Invalid operation. Please enter 'update' or 'remove'.")
    
    # If the key does not exist in the dictionary
    else:
        print(f"The key '{key}' is new.")
        value = input(f"Enter the value for the new key '{key}': ")
        updated_dict[key] = value
        print(f"Key '{key}' with value '{value}' has been added.")
    
    # Display the updated dictionary after each operation
    print(f"Updated dictionary: {updated_dict}")
    print()

# After exiting the loop, display the original, final version, and differences
print("\nProgram terminated.")
print(f"Original dictionary: {original_dict}")
print(f"Final updated dictionary: {updated_dict}")

# Find the differences between the original and updated dictionary
added_keys = set(updated_dict.keys()) - set(original_dict.keys())
removed_keys = set(original_dict.keys()) - set(updated_dict.keys())
modified_keys = {k for k in original_dict.keys() if k in updated_dict and original_dict[k] != updated_dict[k]}

print("\nDifferences:")
print(f"Added keys: {added_keys}")
print(f"Removed keys: {removed_keys}")
print(f"Modified keys: {modified_keys}")