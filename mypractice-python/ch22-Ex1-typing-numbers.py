# Exercise 1: Typing Numbers
# Create a program that prompts the user to enter a number and then displays the type of
# the number entered (e.g., complex, integer, or float). For example, if the user enters 6, the
# output should be int.
# Implement appropriate exception handling for situations where the user enters a string
# that cannot be converted to a number.
def get_number_type(value):
    """Determine the type of the number."""
    try:
        # Try to convert the value to an integer
        num = int(value)
        return "int"
    except ValueError:
        try:
            # If conversion to integer fails, try to convert to float
            num = float(value)
            return "float"
        except ValueError:
            # If conversion to float also fails, it's not a number
            return "Not a number"

def main():
    user_input = input("Enter a number: ")
    number_type = get_number_type(user_input)
    if number_type == "Not a number":
        print("The input is not a valid number.")
    else:
        print(f"The input is of type: {number_type}")

if __name__ == "__main__":
    main()