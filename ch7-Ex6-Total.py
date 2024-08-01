# Exercise 6: And the Total Is...
# Initialize an empty list to store the values
values = []

while True:
    user_input = input("Enter a value (or type 'quit' to end): ").strip().lower()
    
    if user_input == 'quit':
        break
    
    try:
        # Convert the input to a number and add it to the list
        value = float(user_input)
        values.append(value)
    except ValueError:
        print("Invalid input. Please enter a numerical value or 'quit' to end.")

# Calculate the total sum of the values
total_sum = sum(values)

# Display the values used in the calculation and the total sum
print("\nValues used in the calculation:", values)
print("Total sum of the values:", total_sum)