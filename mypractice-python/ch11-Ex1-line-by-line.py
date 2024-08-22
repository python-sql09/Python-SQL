# Exercise 1: Line by Line
# Our ERP banking application has a requirement to splice out the unique records contained
# within a set to make individual rows in a database. Use a for loop to retrieve items from
# the following set and print each item on its own line:
# Define the banking set
banking = {"Checking", "Savings", "Loans", "Dividends", "IRAs"}
# Loop through the set and print each item on a new line
for account_type in banking:
    print(account_type)