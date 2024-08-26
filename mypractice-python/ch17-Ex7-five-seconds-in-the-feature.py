# Exercise 7: Five Seconds in the Future
from datetime import datetime, timedelta
def add_five_seconds():
    # Get the current time
    now = datetime.now()
    # Add five seconds to the current time
    future_time = now + timedelta(seconds=5)
    # Display the result
    print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("Time after five seconds:", future_time.strftime("%Y-%m-%d %H:%M:%S"))
# Test the function
add_five_seconds()