# Exercise 5: Self-­Assessment
# Define a set with at least five elements
original_set = {"apple", "banana", "orange", "grape", "kiwi"}

# Make a copy of the original set for comparison later
updated_set = original_set.copy()

while True:
    # Ask the user for a value
    value = input("Enter a value (or type 'quit' to exit): ").lower()

    if value == "quit":
        break

    # Ask the user for an operation ("add" or "remove")
    operation = input("Do you want to 'add' or 'remove' the value? ").lower()

    if operation == "remove":
        # If the value exists in the set, remove it
        if value in updated_set:
            updated_set.remove(value)
            print(f"Removed '{value}'. Updated set: {updated_set}")
        else:
            print("Sorry, the value does not exist.")
    
    elif operation == "add":
        # If the value exists in the set, display a message
        if value in updated_set:
            print("Your item exists.")
        else:
            # Add the value to the set and display the updated set
            updated_set.add(value)
            print(f"Added '{value}'. Updated set: {updated_set}")
    else:
        print("Invalid operation. Please choose 'add' or 'remove'.")

# When the user enters "quit", display the original and updated sets
print("\nOriginal Set: ", original_set)
print("Final Updated Set: ", updated_set)

# Display the difference between the two sets
difference_set = updated_set - original_set
print("Difference between original and updated set: ", difference_set)