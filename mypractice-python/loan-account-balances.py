# 10.12 Loan account balances
loans = dict()
ctr = 1
while ctr <= 5:
    loan_id = input("Please enter the loan ID for loan "+str(ctr)+": ")
    loan_amt = input("Please enter the loan amount for loan "+str(ctr)+": ")
    loans[loan_id]=loan_amt
    ctr+=1
    for key,value in loans.items():
        print(key,": ", value)