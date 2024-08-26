# 2. Creating Specific DateTime with AM/PM
from datetime import datetime
# Create a specific time (e.g., 9:45 AM)
specific_time = datetime(2024, 8, 24, 9, 45)
# Format the time to 12-hour format with AM/PM
formatted_time = specific_time.strftime("%I:%M %p")
print("Specific time:", formatted_time)