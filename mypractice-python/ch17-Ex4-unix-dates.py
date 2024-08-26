# Exercise 4: Unix Dates
from datetime import datetime
def convert_unix_to_date():
    # Prompt user for a Unix timestamp
    unix_timestamp = input("Enter a Unix timestamp(ex: 1692873600): ")
    try:
        # Convert the Unix timestamp to an integer
        unix_timestamp = int(unix_timestamp)
       # Convert the Unix timestamp to a datetime object
        human_readable_date = datetime.utcfromtimestamp(unix_timestamp)
       # Display the human-readable date
        print("The human-readable date is:", human_readable_date.strftime("%Y-%m-%d %H:%M:%S"))
    except ValueError:
        print("Invalid input. Please enter a valid Unix timestamp.")
# Test the function
convert_unix_to_date()