# Using the logical operators
a = True
print(a)
b = False
print(b)
c = not a
print(c)
d = a or b
print(d)
e = a and b
print(e)

# Is it True or False?
a = input("What is the output of the following operation (True and True)? ")
aTest = True and True
print("True and True = ", aTest)
b = input("What is the output of the following operation (False or False)? ")
bTest = False or False
print("False or False = ", bTest)
c = input("What is the output of the following operation (False and False)? ")
cTest = False and False
print("False and False =", cTest)
d = input("What is the output of the following operation (not False)? ")
dTest = not False
print("not False = ", dTest)
e = input("What is the output of the following operation ( (not False) or \
False )? ")
eTest = ( (not False) or False )
print("(not False) or False = ", eTest)
f = input("What is the output of the following operation ( (not True) and (not \
False) )? ")
fTest = ( (not True) and (not False) )
print("(not True) and (not False) = ", fTest)

