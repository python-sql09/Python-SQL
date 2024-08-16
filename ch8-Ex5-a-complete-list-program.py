# Initial list with at least five elements
my_list = ["Milk", "Bread", "Banana", "Apple", "Butter", "Honey"]

# Store a copy of the original list for comparison later
original_list = my_list.copy()

# Ask for the user's first and last name
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

# Function to display the list
def display_list(lst):
    print("\nCurrent list:")
    for item in lst:
        print(f"- {item}")

# Start a loop to perform add/remove operations until the user quits
while True:
    # Ask the user for a value and operation
    value = input("\nEnter a value (or 'quit' to exit): ")
    
    if value.lower() == "quit":
        break
    
    operation = input("Do you want to add or remove this value? ").lower()

    # Perform the appropriate operation
    if operation == "remove":
        if value in my_list:
            my_list.remove(value)
            print(f"\n'{value}' removed from the list.")
        else:
            print(f"\nError: '{value}' is not in the list.")
        display_list(my_list)
    
    elif operation == "add":
        if value in my_list:
            print(f"\nError: '{value}' already exists in the list.")
        else:
            my_list.append(value)
            print(f"\n'{value}' added to the list.")
        display_list(my_list)
    
    else:
        print("\nInvalid operation. Please enter 'add' or 'remove'.")

# End of loop, display final results
print("\nProgram terminated.")
print(f"\nOriginal list: {original_list}")
print(f"Final list: {my_list}")

# Calculate the difference between the original and final lists
difference = list(set(my_list) - set(original_list))

print(f"\nDifference between the original and final list: {difference}")
print(f"\nThank you, {first_name} {last_name}, for using the program!")