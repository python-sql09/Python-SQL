# Prompt the user for the principal amount, the rate of interest, and the number of days
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate as a fraction (e.g., 0.05 for 5%): "))
days = int(input("Enter the number of days for the loan: "))
# Calculate the simple interest using the formula: interest = principal * rate * days / 365
interest = principal * rate * days / 365
# Display the entered values and the calculated interest
print("\nPrincipal amount:", principal)
print("Annual interest rate:", rate)
print("Number of days for the loan:", days)
print("Simple interest for the life of the loan:", interest)