# 3. Parsing Time Strings with AM/PM
from datetime import datetime
# Parsing a time string with AM/PM
time_string = "09:45 PM"
parsed_time = datetime.strptime(time_string, "%I:%M %p")
print("Parsed time:", parsed_time)