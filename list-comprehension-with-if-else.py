#8.26 List comprehension with if-­else
numbers = [1,2,-1,6,-5,-2]
print(numbers)
label = ["positive" if number>=0 else "negative" for number in numbers]
print(label)