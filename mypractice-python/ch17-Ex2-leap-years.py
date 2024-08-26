# Exercise 2: Leap Years
def is_leap_year():
    # Prompt user for a year
    year = int(input("Enter a year: "))
    # Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
# Test the function with various inputs
result = is_leap_year()
if result:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")