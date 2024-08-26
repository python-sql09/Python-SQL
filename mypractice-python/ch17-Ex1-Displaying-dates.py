# Exercise 1: Displaying Dates
from datetime import datetime
# Get the current date and time
current_datetime = datetime.now()
# Display the current date and time
print("Current date and time:", current_datetime)
# Display the current year
print("Current year:", current_datetime.year)
# Display the current month (as a number, you can also display the name of the month)
print("Current month:", current_datetime.month)
# Display the week number of the year
print("Week number of the year:", current_datetime.strftime("%U"))
# Display the weekday of the week (0 is Monday, 6 is Sunday)
print("Weekday of the week:", current_datetime.weekday())
# Display the day of the year
print("Day of the year:", current_datetime.strftime("%j"))
# Display the day of the month
print("Day of the month:", current_datetime.day)
# Display the day of the week (as a string)
print("Day of the week:", current_datetime.strftime("%A"))