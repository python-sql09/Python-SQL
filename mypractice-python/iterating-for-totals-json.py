# 20.8 Iterating for totals
import json

filename = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/bank_transactions.json'
with open(filename, 'r') as jsonfile:
    data = json.load(jsonfile)

total = 0
total_balance = 0

for each in data:
    if each.get('WITHDRAWAL AMT'):  # Safely access 'WITHDRAWAL AMT' using .get()
        total += float(each['WITHDRAWAL AMT'])
    
    if each.get('BALANCE AMT'):  # Safely access 'BALANCE AMT' using .get()
        total_balance += float(each['BALANCE AMT'])

print("Total Withdrawals: ", total)
print("Total of Balances: ", total_balance)