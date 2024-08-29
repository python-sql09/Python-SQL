# Exercise 2: Current Value
# The program should prompt the user for each of the values and use the following for-
# mula to calculate the current value of the deposit:
# V = P(1 + r/n)^nt
# Where:
# •• V : Value
# •• P : Initial deposit
# •• r : Interest rate as a fraction (e.g., 0.05)
# •• n : The number of times per year interest is calculated
# •• t : The number of years since the initial deposit
def calculate_deposit_value(P, r, n, t):
    """Calculate the current value of the deposit using the compound interest formula."""
    try:
        V = P * (1 + r / n) ** (n * t)
        return V
    except ZeroDivisionError:
        return None

def parse_percentage(percentage):
    """Convert a percentage string to a fraction."""
    try:
        return float(percentage.strip('%')) / 100
    except ValueError:
        raise ValueError("Invalid percentage format. Please enter a number with or without a '%' sign.")

def main():
    # Prompt user for input and handle potential exceptions
    try:
        P = float(input("Enter the initial deposit amount (P): "))
        r_input = input("Enter the interest rate (r) as a percentage (e.g., 5 for 5%): ")
        r = parse_percentage(r_input)
        n = int(input("Enter the number of times interest is calculated per year (n): "))
        t = float(input("Enter the number of years since the initial deposit (t): "))
        if n == 0:
            raise ValueError("The number of times interest is calculated per year (n) cannot be zero.")
        # Calculate the current value of the deposit
        V = calculate_deposit_value(P, r, n, t)
        if V is not None:
            print(f"\nInitial deposit (P): ${P:.2f}")
            print(f"Interest rate (r): {r * 100:.2f}%")
            print(f"Number of times interest is calculated per year (n): {n}")
            print(f"Number of years (t): {t}")
            print(f"Current value of the deposit (V): ${V:.2f}")
        else:
            print("An error occurred during the calculation. Please ensure all inputs are valid.")
    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()