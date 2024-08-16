# Exercise 3: List Deletion
# Present the user with a list of 7–9 items (such as the lists created in the previous exer-
# cises). Prompt the user to enter one item to delete from the list. Delete the named item
# from the list and display the updated list.

'''#Initiliaze a grocery list with existing items
grocery_list = ["Milk", "Bread", "Banana", "apple", "Butter", "Salt", "Honey", "Soap", "Tomato", "Cheese"]
#Display the current grocerry list
print("Current Grocery List: ")
for item in grocery_list:
    print(item)
val = grocery_list.pop(6)
print(grocery_list)
print(val)
'''
# Initial list with 7–9 items
grocery_list = ["Milk", "Bread", "Banana", "Apple", "Butter", "Salt", "Honey", "Soap", "Tomato"]

# Display the list to the user
print("Here is your grocery list:")
for item in grocery_list:
    print(f"- {item}")

# Prompt the user to enter the name of the item they want to delete
item_to_delete = input("\nEnter the name of the item you want to delete: ")

# Check if the item is in the list and delete it
if item_to_delete in grocery_list:
    grocery_list.remove(item_to_delete)
    print(f"\n'{item_to_delete}' has been removed from the list.")
else:
    print(f"\nError: '{item_to_delete}' is not in the list.")

# Display the updated list
print("\nUpdated grocery list:")
for item in grocery_list:
    print(f"- {item}")
