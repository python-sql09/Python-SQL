# 10.23 Updating a dictionary in a single call
info = {
"name": "Enzo",
"accounts":"",
"address":"",
}
print(info)
print("====================")
new_info = {'name' : "Enzo Stephens", 'accounts': ['Checking', 'Savings','Auto Loan'],
'address':'321 Smithfield Lane, New Town, PA, 11876' }
info.update(new_info)
print(info)