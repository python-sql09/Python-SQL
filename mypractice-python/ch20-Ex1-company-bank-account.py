# Exercise 1: Company Bank Account
# Create a dictionary that represents a company bank account with fields for customer_ID,
# name, and account number. Use the json.dumps() function to convert the dictionary into
# a JSON-­encoded object.
import json
# Create a dictionary representing a company bank account
company_bank_account = {
    "customer_ID": "C123456789",
    "name": "Acme Corporation",
    "account_number": "9876543210"
}
# Convert the dictionary into a JSON-encoded object
company_bank_account_json = json.dumps(company_bank_account, indent=4)
# Print the JSON-encoded object
print(company_bank_account_json)