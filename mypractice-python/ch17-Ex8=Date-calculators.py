# Exercise 8: Date Calculators
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def time_duration_calculator():
    print("Time Duration Calculator")
    try:
        # Prompt user for the first duration
        days1 = int(input("Enter the number of days for the first time duration: "))
        hours1 = int(input("Enter the number of hours for the first time duration: "))
        minutes1 = int(input("Enter the number of minutes for the first time duration: "))
        seconds1 = int(input("Enter the number of seconds for the first time duration: "))

        # Prompt user for the second duration
        days2 = int(input("Enter the number of days for the second time duration: "))
        hours2 = int(input("Enter the number of hours for the second time duration: "))
        minutes2 = int(input("Enter the number of minutes for the second time duration: "))
        seconds2 = int(input("Enter the number of seconds for the second time duration: "))

        # Ask for addition or subtraction
        operation = input("Do you want to add or subtract the times? (Enter '+' or '-'): ")

        # Calculate the total time duration
        first_duration = timedelta(days=days1, hours=hours1, minutes=minutes1, seconds=seconds1)
        second_duration = timedelta(days=days2, hours=hours2, minutes=minutes2, seconds=seconds2)

        if operation == '+':
            result = first_duration + second_duration
        elif operation == '-':
            result = first_duration - second_duration
        else:
            print("Invalid operation. Please enter '+' or '-'.")
            return

        # Display the results
        total_seconds = result.total_seconds()
        total_minutes = total_seconds / 60
        total_hours = total_minutes / 60
        total_days = total_hours / 24

        print(f"Result: {result}")
        print(f"{int(total_days)} days, {int(total_hours % 24)} hours, {int(total_minutes % 60)} minutes, {int(total_seconds % 60)} seconds")
        print(f"Total days: {total_days}")
        print(f"Total hours: {total_hours}")
        print(f"Total minutes: {total_minutes}")
        print(f"Total seconds: {total_seconds}")
    
    except ValueError:
        print("Please enter valid numeric values.")

def add_subtract_time_calculator():
    print("Add/Subtract Time from Date Calculator")
    try:
        # Prompt for date and time input
        date_str = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
        date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

        # Prompt for duration to add or subtract
        days = int(input("Enter the number of days: "))
        hours = int(input("Enter the number of hours: "))
        minutes = int(input("Enter the number of minutes: "))
        seconds = int(input("Enter the number of seconds: "))

        # Ask for addition or subtraction
        operation = input("Do you want to add or subtract the time? (Enter '+' or '-'): ")

        duration = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

        # Perform addition or subtraction
        if operation == '+':
            result = date_obj + duration
        elif operation == '-':
            result = date_obj - duration
        else:
            print("Invalid operation. Please enter '+' or '-'.")
            return

        # Display the result with the day of the week
        print("Result:", result.strftime('%Y-%m-%d %H:%M:%S'), result.strftime('(%A)'))

    except ValueError:
        print("Invalid date or time format. Please enter in the format YYYY-MM-DD HH:MM:SS.")

def age_calculator():
    print("Age Calculator")
    try:
        # Prompt for start date and end date
        start_date_str = input("Enter the start date (YYYY-MM-DD): ")
        end_date_str = input("Enter the end date (YYYY-MM-DD): ")

        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

        # Calculate the difference using relativedelta
        diff = relativedelta(end_date, start_date)

        # Display the results
        print(f"Years: {diff.years}, Months: {diff.months}, Days: {diff.days}")
        print(f"Total months: {diff.years * 12 + diff.months}")
        total_days = (end_date - start_date).days
        print(f"Total days: {total_days}")
        print(f"Total hours: {total_days * 24}")
        print(f"Total minutes: {total_days * 24 * 60}")
        print(f"Total seconds: {total_days * 24 * 60 * 60}")

    except ValueError:
        print("Invalid date format. Please enter in the format YYYY-MM-DD.")

def main():
    while True:
        print("\nDate Calculator Menu:")
        print("1. Time Duration Calculator")
        print("2. Add/Subtract Time from Date Calculator")
        print("3. Age Calculator")
        print("4. Clear input and start over")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            time_duration_calculator()
        elif choice == '2':
            add_subtract_time_calculator()
        elif choice == '3':
            age_calculator()
        elif choice == '4':
            continue  # Restart the loop
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Start the program
main()