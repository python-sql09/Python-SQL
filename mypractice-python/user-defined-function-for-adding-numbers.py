# 13.1 A user-defined function for adding numbers
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiple(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2

sum1 = add(100, 200)
sum2 = add(9, 9)
sum3 = subtract(900, 300)
sum4 = subtract(9, 3)
sum5 = multiple(90, 30)
sum6 = multiple(9, 3)
sum7 = divide(90, 30)
sum8 = divide(9, 3)
sum9 = mod(100, 30)

print(sum1)
print(sum2)
print(sum3)
print(sum4)
print(sum5)
print(sum6)
print(sum7)
print(sum8)
print(sum9)