# 1. Using datetime.strftime to Format Time with AM/PM
from datetime import datetime
# Get the current date and time
now = datetime.now()
# Format it to display in 12-hour format with AM/PM
formatted_time = now.strftime("%I:%M %p")  # %I = 12-hour clock, %p = AM/PM
print("Current time:", formatted_time)
