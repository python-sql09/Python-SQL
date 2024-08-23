# 14.11 A sales class
class Sales:
    @staticmethod
    def applySalesTax(amount):
        sales_tax = 0.06
        return amount*(1+sales_tax)
    @staticmethod
    def applySalesTaxMany(amounts):
        out = list()
        sales_tax = 0.06
        out = [amount*(1+sales_tax) for amount in amounts]
        return out
print(Sales.applySalesTax(20))
print(Sales.applySalesTaxMany([10,20,30]))