# Exercise 11: Count the Numbers
# Ask the user for an integer
number = input("Enter an integer: ")

# Initialize a dictionary to store digit frequencies
digit_count = {}

# Compute the frequency of each digit
for digit in number:
    if digit.isdigit():  # Check if the character is a digit
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

# Display the frequency of each digit
for digit, count in digit_count.items():
    if count > 1:
        print(f"{digit} occurs {count} times")
    else:
        print(f"{digit} occurs {count} time")