# 11.9 Searching items in a set
cust_list = {
"Wolf Inc",
"Acme Inc",
"Murray Ltd",
"BankCorps",
"PierBank",
"BankRoad",
"Cashop",
"Welch-Mann",
"Oberbrunner, Hamill and Marvin",
"Faust Inc.",
"Watera",
"Jacobson LLC",
"Micron Computers",
}
print(cust_list)
lower_list = [x.lower() for x in cust_list]
if input("Enter a customer name: ").lower() in lower_list:
    print("The customer name you entered matches an existing customer.")
else:
    print("That name did not match any in our customer list.")