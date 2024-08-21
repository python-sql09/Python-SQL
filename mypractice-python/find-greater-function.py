# 13.2 The find_greater function
def find_greater(numbers,threshold):
    for num in numbers:
        # we only display the numbers that are above the input threshold
        if (num > threshold):
            print(num)

def find_lesser(numbers,threshold):
    for num in numbers:
        # we only display the numbers that are above the input threshold
        if (num < threshold):
            print(num)
    
numbers = [1,5,6,7,10,1,15,18,21]
find_greater(numbers,0) # find all numbers greater than 0
print("------")
find_greater(numbers,5) # find all numbers greater than 5
print("------")
find_greater(numbers,10) # find all numbers greater than 10
print("------")
find_lesser(numbers,5) # find all numbers greater than 0
print("------")
find_lesser(numbers,10) # find all numbers greater than 5
print("------")
find_lesser(numbers,20) # find all numbers greater than 10
