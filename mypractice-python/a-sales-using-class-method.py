# 14.12 Using a class method
class Sales:
    sales_tax = 0.06
    @classmethod
    def applySalesTax(cls,amount):
        return amount*(1+cls.sales_tax)
    @classmethod
    def applySalesTaxMany(cls,amounts):
        out = list()
        sales_tax = 0.06
        out = [amount*(1+cls.sales_tax) for amount in amounts]
        return out
print(Sales.applySalesTax(20))
print(Sales.applySalesTaxMany([10,20,30]))