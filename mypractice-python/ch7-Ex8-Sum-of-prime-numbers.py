# Exercise 8: Sum of Prime Numbers
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if the number can be expressed as the sum of two primes
def can_be_expressed_as_sum_of_primes(num):
    for i in range(2, num):
        if is_prime(i) and is_prime(num - i):
            print(f"{num} = {i} + {num - i}")
            return True
    return False

# Ask the user for an input number
number = int(input("Enter an integer: "))

# Check and display the result
if not can_be_expressed_as_sum_of_primes(number):
    print(f"{number} cannot be expressed as the sum of two prime numbers.")