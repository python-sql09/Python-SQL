# 21.8 Creating a lambda function within a function
def pow_n(n):
    return lambda a: a ** n
pow_2 = pow_n(2)
print(pow_2(6))