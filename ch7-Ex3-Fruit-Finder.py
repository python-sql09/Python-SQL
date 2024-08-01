# Exercise 3: Fruit Finder
fruit_list = ["apple", "banana", "cherry", "gooseberry", "kumquat", "orange","pineapple"]
while True:
    fruit = input("Please Enter the name of a fruit (or type 'stop' to end): ").strip().lower()
    if fruit == 'stop':
        print("Exiting the fruit finder. Goodbye!")
        break 
    if fruit in fruit_list:
        index = fruit_list.index(fruit)
        print(f"The fruit '{fruit}' is at index {index} in the list.")
    else:
        print(f"The fruit '{fruit}' is not in the list. Please try again.")
