# 14.7 Using a class attribute in our account class
class CheckingAccount:
    type = "checking"
    def __init__(self,id,balance):
        self.account_id = id
        self.balance = balance
ch1 = CheckingAccount("ID13434",120000)
ch2 = CheckingAccount("ID13435",180000)
print(ch1.type)
print(ch2.type)