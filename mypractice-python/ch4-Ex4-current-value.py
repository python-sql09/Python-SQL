# Prompt the user for each of the values
P = float(input("Enter the initial deposit (P): "))
r = float(input("Enter the annual interest rate as a fraction (e.g., 0.05 for 5%): "))
n = int(input("Enter the number of times interest is calculated per year (n): "))
t = float(input("Enter the number of years since the initial deposit (t): "))
# Calculate the current value of the deposit using the formula V = P(1 + r/n)^(nt)
V = P * (1 + r / n) ** (n * t)
# Display each of the values entered and the result of the calculation
print("\nInitial deposit (P):", P)
print("Annual interest rate (r):", r)
print("Number of times interest is calculated per year (n):", n)
print("Number of years since the initial deposit (t):", t)
print("Current value of the deposit (V):", V)
