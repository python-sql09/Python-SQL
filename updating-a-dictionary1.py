# 10.22 Updating a dictionary
info = {
"name": "Enzo",
"accounts":"",
"address":"",
}
print(info)
print("====================")
new_name = {'name' : "Enzo Stephens"}
new_accounts = {'accounts': ['Checking', 'Savings','Auto Loan']}
new_address = {'address':'321 Smithfield Lane, New Town, PA, 11876'}
info.update(new_name)
info.update(new_accounts)
info.update(new_address)
print(info)