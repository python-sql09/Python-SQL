# Exercise 7: Multiplication Tables
# Ask the user for an integer value
number = int(input("Enter an integer value: "))

# Display the multiplication table
print(f"\nMultiplication table for {number} from 1 to {number} squared:")
for i in range(1, number ** 2 + 1):
    print(f"{number} x {i} = {number * i}")

# Ask the user for an integer value
number = int(input("Enter an integer value: "))

# Display the multiplication table from 1 to 20
print(f"\nMultiplication table for {number} from 1 to 20:")
for i in range(1, 21):
    print(f"{number} x {i} = {number * i}")