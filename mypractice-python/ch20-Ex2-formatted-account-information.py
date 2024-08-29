# Exercise 2: Formatted Account Information
# Update the company account script from the last practice activity to include the indent
# option to make the output easier to read.
import json

# Create a dictionary representing a company bank account
company_bank_account = {
    "customer_ID": "C123456789",
    "name": "Acme Corporation",
    "account_number": "9876543210"
}
# Convert the dictionary into a JSON-encoded object with formatted output
company_bank_account_json = json.dumps(company_bank_account, indent=6)
# Print the formatted JSON-encoded object
print(company_bank_account_json)