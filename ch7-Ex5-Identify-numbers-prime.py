# Exercise 5: Identify the Numbers
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Identifying all prime numbers between 0 and 100
prime_numbers = [num for num in range(101) if is_prime(num)]
print("Prime numbers between 0 and 100:", prime_numbers)

# Computing the sum of all numbers between 0 and 100
total_sum = sum(range(101))
print("Sum of all numbers between 0 and 100:", total_sum)