user_input = input("Please enter a number: ")

# Check if the input is an integer
if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):
    print("The type of the number is: int")
    
# Check if the input is a float
elif '.' in user_input:
    parts = user_input.split('.')
    if len(parts) == 2 and (parts[0].isdigit() or (parts[0] == '-' and parts[1].isdigit())) and parts[1].isdigit():
        print("The type of the number is: float")

# Check if the input is a complex number
elif 'j' in user_input or 'J' in user_input:
    number = complex(user_input)
    print("The type of the number is: complex")
else:    
    # If no type matches, print not valid
    print("The input is not a valid number")