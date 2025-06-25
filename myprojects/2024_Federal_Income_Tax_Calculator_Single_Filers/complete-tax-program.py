# -------------------------------------------------------------------------------------------
# Project Name: Burger Shop Process Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/2024_Federal_Income_Tax_Calculator_Single_Filers
# Date        : August 21, 2024
# Description : This Python program calculates the federal income tax owed by a single individual
#               in the U.S. for the tax year 2024, based on the IRS tax bracket thresholds.
#               The script considers standard deductions and dependent exemptions before applying
#               marginal tax rates.
# --------------------------------------------------------------------------------------------------
# 2024 Tax Rates
# -------------------------------------------
# Tax Rate    Income for Single Individuals #
# -------------------------------------------
#   10%             Up to $11,600            #             
#   12%             $11,601 to $47,150       # 
#   22%             $47,151 to $100,525      #
#   24%             $100,526 to $191,950     #
#   32%             $191,950 to $243,725    #
#   35%             $243,726 to $609,350    #
#   37%             $609,350 or more        #
#--------------------------------------------

#----------------------------------------------
# Single Person Income-Tax Calculator Program #
#----------------------------------------------
# initialize the variables
max10 = 11600
max12 = 47150
max22 = 100526
max24 = 191950
max32 = 243725
max35 = 609350
tier10_tax = max10 * .1
tier12_tax = tier10_tax + ((max12 - max10) * .12)
tier22_tax = tier12_tax + ((max22 - max12) * .22)
tier24_tax = tier22_tax + ((max24 - max22) * .24)
tier32_tax = tier24_tax + ((max32 - max24) * .32)
tier35_tax = tier32_tax + ((max35 - max32) * .35)
# define user input
gross_inc = float(input("Enter your gross income from your W-2 for 2024: "))
num_dep = int(input("How many dependents are you claiming? "))
# calculate taxable income
tax_income = gross_inc -14600 - (1950 * num_dep)
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
print (tax_income)