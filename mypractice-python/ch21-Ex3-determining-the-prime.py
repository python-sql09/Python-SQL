# Exercise 3: Determining Prime
# Create a script that uses the map() function to determine which integers are prime num-
# bers in an input list of integers.
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to determine prime numbers in a list using map
def determine_primes(input_list):
    return list(map(is_prime, input_list))

# Example usage
input_values = [2, 3, 4, 5, 10, 17, 19, 20, 23]  # Replace with your list of integers
prime_flags = determine_primes(input_values)

# Display the results
print("Original values:", input_values)
print("Prime flags:", prime_flags)

# Showing which numbers are prime
prime_numbers = [num for num, is_prime in zip(input_values, prime_flags) if is_prime]
print("Prime numbers:", prime_numbers)