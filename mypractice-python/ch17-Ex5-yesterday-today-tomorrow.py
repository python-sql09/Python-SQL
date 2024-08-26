# Exercise 5: Yesterday, Today, and Tomorrow
from datetime import datetime, timedelta
def print_yesterday_today_tomorrow():
    # Get today's date
    today = datetime.now()
    # Calculate yesterday's date by subtracting 1 day from today
    yesterday = today - timedelta(days=1)
    # Calculate tomorrow's date by adding 1 day to today
    tomorrow = today + timedelta(days=1)
    # Print the dates in YYYY-MM-DD format
    print("Yesterday's date:", yesterday.strftime("%Y-%m-%d"))
    print("Today's date:", today.strftime("%Y-%m-%d"))
    print("Tomorrow's date:", tomorrow.strftime("%Y-%m-%d"))
# Test the function
print_yesterday_today_tomorrow()