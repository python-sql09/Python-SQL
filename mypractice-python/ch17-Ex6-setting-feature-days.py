# Exercise 6: Setting Future Days
from datetime import datetime, timedelta
def print_next_five_days():
    # Get today's date
    today = datetime.now()
    # Print the date for the next five days
    print("Starting from today, the dates for the next five days are:")
    for i in range(6):
        future_date = today + timedelta(days=i)
        print(f"Day {i}: {future_date.strftime('%Y-%m-%d')}")
# Test the function
print_next_five_days()