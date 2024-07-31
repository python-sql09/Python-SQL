#Prompting for the income
# define user input
gross_inc = float(input("Enter your gross income from your W-2 for 2020: "))
# print(gross_inc)
# Adding additional prompt
num_dep = int(input("How many dependents are you claiming? "))
# print(num_dep)
# Adding the taxable income formula
# calculate taxable income
tax_income = gross_inc - 12200 - (2000 * num_dep)
print (tax_income)
# calculate tax due
tax_due = tax_income * 0.1
# print the result
print(tax_due)




