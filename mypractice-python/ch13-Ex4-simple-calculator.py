# Exercise 4: Simple Calculator
# Design a function called simple_calculator that performs basic math operations
# (addition, subtraction, multiplication, division) on two operands. Use the function to cre-
# ate a program that allows the user to perform simple calculations on two numbers. For
# example, the program should allow the user to input two numbers of their choice, perform
# the selected operation on the numbers, and display the result.

def simple_calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

# Main program
while True:
    try:
        # Get the two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        # Get the operation from the user
        operation = input("Enter the operation (+, -, *, /): ")
        # Perform the calculation using the simple_calculator function
        result = simple_calculator(num1, num2, operation)
        # Display the result
        print(f"The result of {num1} {operation} {num2} is: {result}")
        # Ask if the user wants to perform another calculation
        repeat = input("Do you want to perform another calculation? (yes/no): ").lower()
        if repeat != "yes":
            break

    except ValueError:
        print("Invalid input. Please enter valid numbers.")