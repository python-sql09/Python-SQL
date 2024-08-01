# Using range() with for
for number in range (100, 1000):
    if number % 50 == 0:
        print(number)

# Using while without range()
number = 100
while number <= 1000:
    if number % 50 == 0:
        print(number)
    number += 1