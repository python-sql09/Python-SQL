#Variables for a banking application
acctBal=13445;
savInterest=.025;
months=12;
alphanum=1+52.4j;
print(acctBal);
print(savInterest);
print(months);
print(alphanum);

# Updated banking program with numeric variables
acctBal = 13445; # account balance
locBal = 16000; # credit balance
savBal = 4000; #savings balance
savInterest = .025;
locInterest = .098;
months = 12;
years = 8.5;
numString = "12345"
result1 = acctBal+savBal-locBal;
print(result1); 
result2 = acctBal-locBal*locInterest;
print(result2); 
result3 = savBal*months*savInterest;
print(result3); 
result4 = acctBal/savBal/locBal;
print(result4);
result5 = savBal*1+savInterest/months**years;
print(result5)

#Fixing the bank application calculations
acctBal = 13445;
locBal = 16000;
savBal = 4000;
savInterest = .025;
locInterest = .098;
months = 12;
years = 8.5;
numString = "12345"
compInt = savBal*((1 + (savInterest/months))**(months*years))
print(compInt)
result1 = (savBal+acctBal)- locBal
print(result1)
result2 = (acctBal-locBal)*locInterest
print(result2);
result3 = ((savInterest/months)+1)**(months*years)
print(result3);

#The banking application with rounding added
acctBal = 13445;
locBal = 16000;
savBal = 4000;
savInterest = .025;
locInterest = .098;
months = 12;
years = 8.5;
numString = "12345"
compInt = savBal * ((1 + (savInterest/months))**(months*years))
print(round(compInt,2))
result1 = (savBal+acctBal)-locBal
print(result1)
result2 = (acctBal-locBal)*locInterest
print(round(result2,2));
result3 = ((savInterest/months)+1)**(months*years)
print(result3);
result4 = ((locInterest*months*years)+1)*locBal
print(round(result4,1))

#A new banking Python script
import math;
loan1=12383.89
loan2=48339.99
roundLoanA = math.ceil(loan1*.078)
#print(roundLoanA)
roundloanB = math.floor(loan2*.19)
#print(roundloanB)
print(roundLoanA+roundloanB)

# Querying a banking customer
savings = input("Do you have a savings account?: ");
checking = input("Do you have a checking account?: ");
opensave = input("Would you like to open a savings account?: ")
opencheck = input("Would you like to open a checking account?: ")
print(savings);
print(type(savings));
print(checking);
print(type(checking));
print(opensave);
print(type(opensave));
print(opencheck);
print(type(opencheck));

# formula to calculate the current value of the deposit:
# V = P(1 + r/n)^nt
# V = value
# P = initial deposit
# r = interest rate as a fraction (e.g., 0.05)
# n = the number of times per year interest is calculated
# t = the number of years since the initial deposit
