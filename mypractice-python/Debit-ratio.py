#Calculating a debt ratio
monthlyDebt = input("Enter the monthly debt payments: ");
grossIncome = input("Enter the gross monthly income: ");
#Convert the strings to integers
debtInt = int(monthlyDebt);
incomeInt = int(grossIncome);
diRatio = debtInt / incomeInt;
print(diRatio);
