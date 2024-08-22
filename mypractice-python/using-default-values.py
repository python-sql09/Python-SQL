# 13.6 Using a default value
def find_greater(transactions,threshold=0):
    for trans in transactions:
        # we only display the transactions that are above the input threshold
        if (trans > threshold):
            print(trans)
transactions = [10,15,15,27,100,10]
find_greater(transactions)# find all numbers greater than 0
print("------")
find_greater(transactions,15) # find all numbers greater than 15