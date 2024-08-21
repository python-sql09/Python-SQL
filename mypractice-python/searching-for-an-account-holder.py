# 10.16 Searching for an account holder
accounts = {
'001': 'Daniel Atkins',
'002': 'Rachael Ingram',
'003': 'Caiden McKee',
'004': 'Tiara Johns',
'005': 'Dawson Drake',
'006': 'Lisa Short',
'007': 'Karlee Richard',
'008': 'Kaden Knox',
'009': 'Kendrick Galvan',
'010': 'Aidyn Herrera'
}
account = accounts.get(input("Please enter an account number (e.g. 001): "))
if account == None:
    print("Account not found.")
else:
    print(account)