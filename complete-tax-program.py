# Our completed tax program
# initialize the variables
max10 = 9875
max12 = 40125
max22 = 85525
max24 = 163300
max32 = 207350
max35 = 518400
tier10_tax = max10 * .1
tier12_tax = tier10_tax + ((max12 - max10) * .12)
tier22_tax = tier12_tax + ((max22 - max12) * .22)
tier24_tax = tier22_tax + ((max24 - max22) * .24)
tier32_tax = tier24_tax + ((max32 - max24) * .32)
tier35_tax = tier32_tax + ((max35 - max32) * .35)
# define user input
gross_inc = float(input("Enter your gross income from your W-2 for 2020: "))
num_dep = int(input("How many dependents are you claiming? "))
# calculate taxable income
tax_income = gross_inc -12200 - (2000 * num_dep)
if tax_income <=0:
    tax_due = 0
elif tax_income <= max10:
    tax_due = tax_income * 0.1
elif tax_income <= max12:
    tax_due = tier10_tax + ((tax_income - max10) * .12)
elif tax_income <= max22:
    tax_due = tier12_tax + ((tax_income - max12) * .22)
elif tax_income <= max24:
    tax_due = tier22_tax + ((tax_income - max22) * .24)
elif tax_income <= max32:
    tax_due = tier24_tax + ((tax_income - max24) * .32)
elif tax_income <= max35:
    tax_due = tier32_tax + ((tax_income - max32) * .35)
elif tax_income > max35:
    tax_due = tier35_tax + ((tax_income - max35) * .37)
# report the results to the user
print("Your gross income is $" + str(gross_inc) + ".")
print("You have " + str(num_dep) + " dependents.")
print("Your taxable income is $" + str(tax_income) + ".")
print("Your tax due is $" + str(int(tax_due)) + ".")
