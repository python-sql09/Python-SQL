# 10.20 ERP app to check for ssn key
account_info = {
"owner": "Violet Duffy",
"accounts": ['checking','savings', 'loan'],
"address": "123 Main Street, Louisville, KY"
}
user_input = input("Please enter a key to search: ")
if user_input in account_info.keys():
    print(user_input + " exists in the account. The value is set to ", account_info[user_input])
else:
    print(user_input + " does not exist in the user account.")