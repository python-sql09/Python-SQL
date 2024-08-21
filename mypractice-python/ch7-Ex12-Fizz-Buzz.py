# Ask the user for a number
target_count = int(input("How many fizzing and buzzing units do you need in your life? "))

# Initialize counters
count = 0
fizz_buzz_count = 0

# Perform Fizz Buzz until the count of fizz, buzz, and fizz buzz reaches the target
while fizz_buzz_count < target_count:
    if count % 3 == 0 and count % 5 == 0:
        print("fizz buzz")
        fizz_buzz_count += 1
    elif count % 3 == 0:
        print("fizz")
        fizz_buzz_count += 1
    elif count % 5 == 0:
        print("buzz")
        fizz_buzz_count += 1
    else:
        print(count)
    
    count += 1

# Print the final line
print("TRADITION!!")