# 20.5 Converting from JSON to a dictionary
import json
x = """{
    "Name": "Cheyanne Kemp",
    "Contact Number": 7867567898,
    "Email": "ckemp@gmail.com",
    "Services":["Checking", "Savings", "Auto Loan"]
}"""
user_data = json.loads(x)
print(user_data['Email'])