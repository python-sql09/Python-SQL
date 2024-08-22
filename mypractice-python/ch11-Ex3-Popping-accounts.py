# Exercise 3: Popping Accounts
# Initial set of account numbers
account_numbers = {"L000012", "L000023", "S0001243", "C122399"}

# Display the set and the number of items in the set
print("Account Numbers:", account_numbers)
print("Number of items in the set:", len(account_numbers))

# Ask the user if they want to remove an item from the set
while len(account_numbers) > 0:
    remove_item = input("Do you want to remove an item from the set? (yes/no): ").lower()

    if remove_item == "yes":
        # Check if there is at least one item in the set
        if len(account_numbers) > 0:
            # Remove a random item from the set using pop()
            removed_item = account_numbers.pop()
            print(f"Removed item: {removed_item}")
            print("Updated set:", account_numbers)
            print("Number of items in the set:", len(account_numbers))
        else:
            print("No items left in the set.")
            break
    elif remove_item == "no":
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

# If the set is empty, display a message
if len(account_numbers) == 0:
    print("The set is empty. No more items to remove.")
