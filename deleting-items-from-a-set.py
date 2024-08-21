# 11.13 Deleting items from a set
names = {"Savion", "Amiah", "Niko", "Jackson"}
print(names)
user_input = input("Please enter a name to remove: ")
if user_input in names:
    names.remove(user_input)
    print(names)
else:
    print("You did not enter a name in the set. Currently the names in the set are " +
    str(names))