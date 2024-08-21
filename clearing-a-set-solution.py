# 11.15 Clearing a set solution
names_1 = {"Ben", "Gary", "Jaiden"}
names_2 = {"Sandra", "Rudy", "Marc"}
names_3 = {"Brittany", "Hope", "Jaylen"}
print("names_1", names_1)
print("names_2", names_2)
print("names_3", names_3)
user_input = input("Please enter a name that corresponds to a name in the list: ")
if user_input in names_1:
    names_1.clear()
    print("names_1 set cleared")
elif user_input in names_2:
    names_2.clear()
    print("names_2 set cleared")
elif user_input in names_3:
    names_3.clear()
    print("names_3 set cleared")
else:
    print("The input does not exist as a variable in any of the sets.")