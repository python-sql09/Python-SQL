# 13.3 Creating a function to find numbers divisible by a factor
def find_div(transactions,factor):
    for num in transactions:
        if (num % factor == 0):
            print(num)

transactions = [1,5,5,7,10,28,9,12,15,18,21,24]
print("Factor of 3:")
find_div(transactions,3) # find all transactions divisible by 3
print("Factor of 2:")
find_div(transactions,2) # find all transactions divisible by 2
print("Factor of 4:")
find_div(transactions,4) # find all transactions divisible by 4