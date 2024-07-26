# Simple Interest formula
# Simple interest = principal * rate * days / 365
#Calculating the simple interest
acctBal = input("Please enter an account balance: ");
intRate = input("Please enter an interest rate: ");
time = input("Please enter a period of time in years: ");
acctInt = int(acctBal);
rateInt = float(intRate);
timeInt = int(time);
result = acctInt * rateInt * timeInt;
acctBal = result + acctInt;
print(acctBal);
