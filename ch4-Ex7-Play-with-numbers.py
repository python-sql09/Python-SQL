import math

# Prompt the user for a number
user_input = float(input("Please enter a number: "))
# Calculate the Boolean of the number
boolean_value = bool(user_input)
# Calculate the binary equivalent of the number (if it's an integer)
if user_input.is_integer():
    binary_value = bin(int(user_input))
else:
    binary_value = "undefined for non-integers"
# Calculate the square root of the number
sqrt_value = math.sqrt(user_input)
# Display the results to the user
print(f"\nYou selected {user_input}.")
print(f"The Boolean of your number is {boolean_value}.")
print(f"The binary equivalent of your number is {binary_value}.")
print(f"The square root of your number is {sqrt_value:.3f}.")
