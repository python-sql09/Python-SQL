#•• Arithmetic operators
#•• Comparison (relational) operators
#•• Assignment operators
#•• Logical operators
#•• Bitwise operators
#•• Membership operators
#•• Identity operators

#•• Arithmetic operators
#•• Addition (+)
#•• Subtraction (-­)
#•• Multiplication (*)
#•• Division (/)
#•• Modulus (%)
#•• Floor division (//)
#•• Exponents (**)

#Arithmetic operations
a = 50
b = 6
c = a + b # sum of a and b
d = a - b # difference between a and b
e = a * b # product of a and b
f = a / b # quotient of a and b
g = a // b # floored quotient of a and b
h = a % b # remainder of a / b
i = a ** b # a to the power of b
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

#Predict the output of the calculations
a = 10
b = 20
c = 30
d = a - b * c
print("a - b * c:", d)
e = (a -b) * c
print("a -(b * c)", e)
f = a % b ** c
print("a % b ** c:", f)
g = (a % b) ** c
print("(a % b) ** c:", g)

#•• Compound Interest Calculation: (S = Savings, m = months, i = savings interest, y = years)
#•• S(1 + (i / m))^my
#•• pow(a, b): Calculates a to the power of b; alternative of a**b
#•• round(a): Rounds a to the nearest integer
#•• round(a, b): Rounds a to b decimal points
#•• bin(a): Converts a decimal value a to its binary value

#Using Python math functions
a = 10
b = 20
c = 15.578
d = 15.494
e = 15.50000
f = pow(a, b)
g = round(c)
h = round(d)
i = round(e)
j = round(d, 1)
k = bin(a)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)

# ceil(x)    Returns the smallest integer greater than or equal to x
# cos(x)     Returns the cosine of x where x is in radians      
# e          Returns Euler’s number (2.718....)
# fabs(x)    Returns the absolute value of x
# floor(x)   Rounds a float value of x down to the closest integer and returns that value
# gcd(x, y)  Returns the greatest common divisor of two integers (x and y)
# isqrt(x)   Returns a square root of x after it has been rounded downward to the nearest integer
# pi         Returns the mathematical constant for pi, which is the ratio of the circumference of a circle to its diameter (3.141592653589793)
# pow(x, y)  Returns x raised to the power of y
# sin(x)     Returns the sin of x where x is in radians
# sqrt(x)    Returns the square root of x
# tan(x)     Returns the tangent of x where x is in radians
# trunc(x)   Removes all values to the right of the decimal point in x to create an integer, which is returned

#Using math module functions
import math
 #we need to import the math module before using it
a = 6.1
print(a)
b = math.trunc(a) #the integral part of the float
print(b)
c = math.floor(a) #round down
print(c)
d = math.ceil(a) #round up
print(d)
print(math.pi) #print the value of pi






