# Exercise 4: For Every Season...
# Ask the user what season it is
season = input("What season is it? (fall, autumn, winter, spring, or summer): ").strip().lower()
# Determine the output based on the user's input
if season == "fall" or season == "autumn":
    print("I bet the leaves are pretty there!")
elif season == "winter":
    print("I hope you’re ready for snow!")
elif season == "spring":
    print("I can smell the flowers!")
elif season == "summer":
    print("Make sure your AC is working!")
else:
    print("I don’t recognize that season.")