# Exercise 4: Using a Calculator in Class
class SimpleCalculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2

def calculator_program():
    calc = SimpleCalculator()

    print("Welcome to the Simple Calculator!")
    print("You can perform addition (+), subtraction (-), multiplication (*), and division (/).")
    print("To exit the program, type 'Quit' or 'Exit'.")

    while True:
        user_input = input("\nEnter two numbers and an operator (e.g., '5 + 3') or 'Quit' to exit: ")

        if user_input.lower() in ["quit", "exit"]:
            print("Thank you for using the Simple Calculator. Goodbye!")
            break

        # Parse input
        try:
            num1, operator, num2 = user_input.split()
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please enter in the format '5 + 3' or 'Quit' to exit.")
            continue

        # Perform calculation
        if operator == '+':
            result = calc.add(num1, num2)
        elif operator == '-':
            result = calc.subtract(num1, num2)
        elif operator == '*':
            result = calc.multiply(num1, num2)
        elif operator == '/':
            result = calc.divide(num1, num2)
        else:
            print("Invalid operator. Please use +, -, *, or /.")
            continue

        # Display result
        print(f"The result of {num1} {operator} {num2} is: {result}")

# Run the calculator program
calculator_program()