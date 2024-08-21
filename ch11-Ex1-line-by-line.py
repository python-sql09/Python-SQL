# Exercise 1: Line by Line
# Our ERP banking application has a requirement to splice out the unique records contained
# within a set to make individual rows in a database. Use a for loop to retrieve items from
# the following set and print each item on its own line:
banking = {"Checking","Savings","Loans","Dividends","IRAs"}
for bank in banking:
    print(bank)