# 14.4 Using methods in our banking app
class BankCustomer:
    def __init__(self,c_id,fname,lname):
        self.first_Name=fname
        self.customer_ID=c_id
        self.last_Name=lname
    def display_info(self):
        print("Customer's first name is " + self.first_Name)
        print("Customer's last name is " +     self.last_Name)
        print("Customer's ID is " + str(self.customer_ID))

class BankAccount:
    def __init__(self,a_id,name,type):
        self.account_ID = a_id
        self.account_Name=name
        self.account_Type= type
    def display_info(self):
        print("The account name is " + self.account_Name)
        print("The account type is " +    self.account_Type)
        print("Account ID is " + str(self.account_ID))
# Set up customer1
customer1 = BankCustomer(100004,"Layla","Brennan")
# Set up customer2
customer2 = BankCustomer(100005,"Moises","Cardenas")
# Set up customer3
customer3 = BankCustomer(100006,"Maria","Pierce")
# Set up account1
account1 = BankAccount(1004,"Layla's Account","Checking")
customer1.display_info()
customer2.display_info()
customer3.display_info()
account1.display_info()