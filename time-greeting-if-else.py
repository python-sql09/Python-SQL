import time

# Get the current time in hours
current_hour = int(time.strftime('%H'))

# Get user's name
name = input("Hi! Please enter your name: ")

# Determine the appropriate greeting
if current_hour < 12:
    greeting = "Good morning"
elif 12 <= current_hour < 17:
    greeting = "Good afternoon"
elif 17 <= current_hour < 21:
    greeting = "Good evening"
else:
    greeting = "Good night"

# Print the greeting
print(greeting + ", " + name + "!")