# Exercise 2: Shopping List
# Present the user with an existing list of items (such as a shopping list for the grocery store)
# and prompt the user for 2–4 more items to add to the list. Update the list with the new
# items and display the updated list

'''#Initiliaze a grocery list with existing items
grocery_list = ["Milk", "Bread", "Banana", "apple", "Butter", "Salt"]
#Display the current grocerry list
print("Current Grocery List: ")
for item in grocery_list:
    print(item)
num_items = int(input("How many new grocery items would you like to add(3 or 6)?"))
for new_items in range(num_items):
    n_item = input(f"Enter item {new_items+1}: ")
    grocery_list.append(n_item)
for new_old_grocery in grocery_list:
    print(new_old_grocery)
'''

# Initial shopping list
shopping_list = ["Milk", "Bread", "Banana", "Apple", "Butter", "Boost"]

# Display the current shopping list
print("Here is your current shopping list:")
for item in shopping_list:
    print(f"- {item}")

# Prompt the user to enter 3–6 new items
num_items_to_add = int(input("\nHow many items would you like to add (3-6)? "))

# Ensure the user adds a valid number of items
if 3 <= num_items_to_add <= 6:
    for i in range(num_items_to_add):
        new_item = input(f"Enter item {i + 1}: ")
        shopping_list.append(new_item)
    
    # Display the updated shopping list
    print("\nUpdated shopping list:")
    for item in shopping_list:
        print(f"- {item}")
else:
    print("Error: Please enter a number between 2 and 4.")




