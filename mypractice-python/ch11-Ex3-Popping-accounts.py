# Exercise 3: Popping Accounts
account_numbers = {"L000012","L000023","S0001243","C122399" }
# Create a copy of the original dictionary for modification
updated_account = account_numbers.copy()

print("Welcome to the set program! Type 'quit' to exit.")

while True:
    # Ask the user for a key
    acc_no = input("Enter a account number: ")
    
    # Exit the loop if the user types 'quit'
    if acc_no.lower() == "quit":
        break
    
    # If the key exists in the dictionary
    if acc_no in updated_account:
        print(f"The key '{acc_no}' already exists with value '{updated_account[acc_no]}'")
        operation = input("Do you want to 'update' or 'remove' this key? ").lower()
        
        if operation == "remove":
            # Remove the key-value pair from the dictionary
            updated_account[acc_no].pop()   #del updated_dict[key]
            print(f"Account Number '{acc_no}' has been removed.")
        
        elif operation == "update":
            # Ask for a new value and update the dictionary
            new_value = input(f"Enter the new account number '{acc_no}': ")
            updated_account[acc_no] = new_value
            print(f"Account Number '{acc_no}' has been updated with value '{new_value}'")
        
        else:
            print("Invalid operation. Please enter 'update' or 'remove'.")
    
    # If the key does not exist in the dictionary
    else:
        print(f"The Account Number '{acc_no}' is new.")
        value = input(f"Enter the new account number '{acc_no}': ")
        updated_account[acc_no] = value
        print(f"Account Number '{acc_no}' with value '{value}' has been added.")
    
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