# Exercise 3: The Past
from datetime import datetime, timedelta
def subtract_five_days():
    # Prompt user for a date in the format YYYY-MM-DD
    user_input = input("Enter a date (YYYY-MM-DD) or press Enter to use the current date: ")
    # Check if user provided a date or not
    if user_input:
        # Convert the input string to a date object
        try:
            user_date = datetime.strptime(user_input, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            return
    else:
        # Use the current date if no input is provided
        user_date = datetime.now()
    # Subtract 5 days
    new_date = user_date - timedelta(days=5)
    # Display the result
    print("The new date is:", new_date.strftime("%Y-%m-%d"))
# Test the function
subtract_five_days()
