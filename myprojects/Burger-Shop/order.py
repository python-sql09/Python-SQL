import os

class order:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.payment_method = None
        self.total_price = 0.0

    def add_item(self, item):
        self.items.append(item)

    def get_price(self):
        self.total_price = 0.0
        for item in self.items:
            self.total_price += item.get_price()
        return self.total_price

    def choose_payment_method(self):
        print("Please choose a payment method:")
        print("1. Cash")
        print("2. Credit Card")
        choice = input("Enter 1 for Cash or 2 for Credit Card: ")
        if choice == '1':
            self.payment_method = "Cash"
        elif choice == '2':
            self.payment_method = "Credit Card"
            if not self.check_card_balance():
                print("Sorry, your card doesn't have enough balance. Payment failed.")
                return False
        else:
            print("Invalid choice. Defaulting to Cash.")
            self.payment_method = "Cash"
        return True
    
    def check_card_balance(self):
        # Simulate checking card balance
        balance = float(input("Enter card balance: "))
        return balance >= self.get_price()

    def save_transaction(self):
        # Define the folder where the bill should be saved
        folder = "/home/linuxdeepa/python-sql09/Python-SQL/myprojects/Burger-Shop/bills"
        
        # Check if the folder exists, if not, create it
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        # Define the full path to the file inside the folder
        file_path = os.path.join(folder, f"{self.name}_bill.txt")
        
        # Create the bill content
        with open(file_path, "w") as file:
            file.write("==========================================\n")
            file.write(f"Bill for {self.name}\n")
            file.write("==========================================\n")
            for item in self.items:
                file.write(f"{item}\n")
            file.write("------------------------------------------\n")
            file.write(f"Total Price: ${self.get_price():.2f}\n")
            file.write(f"Payment Method: {self.payment_method}\n")
            file.write("==========================================\n")
        
        print(f"Bill saved as {file_path}")

    def __str__(self):
        s = [str(item) for item in self.items]
        return "\n".join(s)

    def display(self):
        print("==========================================")
        print(f"Order Summary for {self.name}")
        print("==========================================")
        for item in self.items:
            print("--------------------------------------")
            print(str(item))
        print("------------------------------------------")
        print(f"Total Price: ${self.get_price():.2f}")
        print(f"Payment Method: {self.payment_method}")
        print("==========================================")