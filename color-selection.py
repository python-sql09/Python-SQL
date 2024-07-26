#Using elif
color="morning"
if color=="red":
    print("The color is red.")
elif color=="blue":
    print("The color is blue.")
elif color=="yellow":
    print("The color is yellow.")
else:
    print("Please enter a valid color.")

# Selecting a color
color=input("Please enter a color [red, green, yellow, blue, pink]: ")
if color == "red":
    print("The color is red.")
elif color == "green":
    print("The color is green.")
elif color == "yellow":
    print("The color is yellow.")
elif color == "blue":
    print("The color is blue.")
elif color == "pink":
    print("This color is pink.")
else:
    print("Please enter a valid color that is on the list.")

# Selecting a color with if-­ else
color=input("Please enter a color [red, green, yellow, blue, pink]: ")
if color == "red":
    print("The color is red.")
else:
    if color == "green":
        print("The color is green.")
    else:
        if color == "yellow":
            print("The color is yellow.")
        else:
            if color == "blue":
                print("The color is blue.")
            else:
                if color == "pink":
                    print("This color is pink.")
                else:
                    print("Please enter a valid color that is on the list.")
