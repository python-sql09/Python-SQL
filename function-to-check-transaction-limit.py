# 13.4 Function to check a transaction limit
def check_transaction_limit(amount):
    # checks if the transaction exceeds the limit
    if amount > 10000:
        print("Above maximum transaction limit!")
    else:
        print("Transaction is within the limit.")
    
# using the above defined function, we can now check the transaction limits
check_transaction_limit(5000)
check_transaction_limit(13000)