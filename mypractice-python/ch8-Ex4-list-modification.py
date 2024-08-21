# Exercise 4: List Modification
# Present the user with a list of 7–9 items (such as the lists created in the previous exer-
# cises). Prompt the user to select one item from the list to update, along with the new
# value for that item. Change the item’s value and display the new list to the user.

# Initial grocery list
grocery_list = ["Milk", "Bread", "Banana", "Apple", "Butter", "Salt", "Honey", "Soap", "Tomato", "Cheese"]

# Display the list to the user
print("Here is your grocery list:")
for index, item in enumerate(grocery_list):
    print(f"{index + 1}. {item}")

# Prompt the user to select an item by its index
item_index = int(input("\nEnter the number of the item you want to update (1-10): ")) - 1

# Check if the selected index is valid
if 0 <= item_index < len(grocery_list):
    # Prompt the user for the new value
    new_value = input(f"Enter the new value for {grocery_list[item_index]}: ")

    # Update the selected item with the new value
    grocery_list[item_index] = new_value

    # Display the updated list to the user
    print("\nUpdated grocery list:")
    for index, item in enumerate(grocery_list):
        print(f"{index + 1}. {item}")
else:
    print("Invalid selection! Please choose a number from 1 to 10.")
