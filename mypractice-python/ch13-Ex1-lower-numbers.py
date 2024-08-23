# Exercise 1: Lower Numbers
# Step 1: Accept at least five and no more than ten integers from the user
numbers = []

while len(numbers) < 10:
    try:
        # Prompt the user to input a number
        number = int(input(f"Enter number {len(numbers) + 1}: "))
        numbers.append(number)
        
        # If the user has entered at least 5 numbers, give the option to stop
        if len(numbers) >= 5:
            stop_input = input("Do you want to stop input? (yes/no): ").lower()
            if stop_input == "yes":
                break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Step 2: Calculate the average of the numbers
if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    print(f"\nThe average of the entered numbers is: {average:.2f}")
    print(f"\nThe total of the entered numbers is: {sum(numbers):.2f}")
    # Step 3: Define the find_lower function
    def find_lower(numbers_list, threshold):
        # Find and display numbers that are lower than the threshold
        lower_numbers = [num for num in numbers_list if num < threshold]
        
        print("\nNumbers lower than the threshold:")
        for num in lower_numbers:
            print(num)
    
    # Call the find_lower function with the list and the average as the threshold
    find_lower(numbers, average)
else:
    print("No numbers were entered.")