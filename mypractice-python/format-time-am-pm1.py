from datetime import datetime
# Get current date and time
now = datetime.now()
# Format date and time with AM/PM
formatted_datetime = now.strftime("%Y-%m-%d %I:%M %p")
print("Formatted date and time:", formatted_datetime)