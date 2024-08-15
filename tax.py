'''tax_income = 4000 
tax_due = tax_income * 0.1 
# print the result 
print(tax_due)'''

'''tax_income = 35000 
if tax_income <= 11600: 
	tax_due = tax_income * 0.1 
tax_due = (11600 * .1) + ((tax_income - 11600) * .12)
# print the result 
print(tax_due)'''

'''tax_income = 35000 
if tax_income <= 11600: 
	tax_due = tax_income * 0.1 
elif tax_income <= 47150: 
	tax_due = (11600 * .1) + ((tax_income - 11600) * .12) 
# print the result 
print(tax_due)'''

'''tax_income = 80000 
if tax_income <= 11600: 
	tax_due = tax_income * 0.1
elif tax_income <= 47150: 
	tax_due = (11600 * .1) + ((tax_income - 11600) * .12) 
elif tax_income <= 100525: 
	tax_due = (11600 * .1) + ((47150 - 11600) * .12) + (tax_income - 47150) * .22 
# print the result 
print(tax_due)'''

tax_income = 150000 
if tax_income <= 11600: 
	tax_due = tax_income * 0.1 
elif tax_income <= 47150: 
	tax_due = (11600 * .1) + ((tax_income - 11600) * .12) 
elif tax_income <= 100525: 
	tax_due = (11600 * .1) + ((47150 - 11600) * .12) + ((tax_income - 47150) * .22) 
elif tax_income <= 191950: 
    tax_due = (11600 * .1) + ((47150 - 11600) * .12) + ((100525 - 47150) * .22) + ((tax_income - 100525) * .24) 
# print the result 
print(tax_due)