# Exercise 2: Cats or Dogs
# Ask the user if they own any cats
cats = input("Do you own any cats? (Yes/No): ").strip().lower()
# Ask the user if they own any dogs
dogs = input("Do you own any dogs? (Yes/No): ").strip().lower()
# Check the user's responses and output the appropriate message
if cats == "yes" and dogs == "yes":
    print("You must really love pets!")
if cats != "yes" or dogs != "yes":
    print("Maybe you need more pets.")

# Exercise 2: Cats or Dogs
# Ask the user if they own any cats
cats = input("Do you own any cats? (Yes/No): ").strip().lower()
# Ask the user if they own any dogs
dogs = input("Do you own any dogs? (Yes/No): ").strip().lower()
# Check the user's responses and output the appropriate message
if cats == "yes" and dogs == "yes":
    print("You must really love pets!")
else:
    print("Maybe you need more pets.")