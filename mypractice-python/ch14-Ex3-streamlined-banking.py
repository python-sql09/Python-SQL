# Exercise 3: Streamlined Banking
class BankAccount:
    def __init__(self, account_number, account_type, balance=0.0):
        self.account_number = account_number
        self.account_type = account_type  # e.g., Checking, Savings
        self.balance = balance
    
    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ${self.balance:.2f}")

class BankCustomer:
    def __init__(self, name, customer_id, accounts):
        self.name = name
        self.customer_id = customer_id
        self.accounts = accounts  # List of BankAccount objects
    
    def display(self):
        print(f"Customer Name: {self.name}")
        print(f"Customer ID: {self.customer_id}")
        print("Accounts:")
        for account in self.accounts:
            account.display_account_info()
            print()  # Line break between account details

# Example: Creating bank accounts
account1 = BankAccount("A1152254", "Checking", 2500.75)
account2 = BankAccount("A1155626", "Savings", 10000.00)
account3 = BankAccount("A1152278", "Checking", 500.50)

# Example: Creating bank customers
customer1 = BankCustomer("Julia Juarez", "C0001", [account1, account3])
customer2 = BankCustomer("Whitney Solomon", "C0002", [account2])

# Display customer information
customer1.display()
customer2.display()