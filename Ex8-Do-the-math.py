# Initialize a list to store the five integers
numbers = []
# Prompt the user for five integers
for i in range(5):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)
# Perform calculations
product = 1
for num in numbers:
    product *= num
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
# Display the results
print("\nCalculations:")
print(f"Product of the integers: {product}")
print(f"Sum of the integers: {total_sum}")
print(f"Average of the integers: {average:.2f}")