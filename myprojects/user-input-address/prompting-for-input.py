# 12.1 Prompting for input
# Name: Deepa Ponnusamy
# Date created: Augest 21, 2024
# Purpose: Code-­along for Python course
user_address = input("Enter an address (e.g., 123 Main Street): ")
#check that string is not empty (after removing leading and trailing spaces)
if user_address.strip():  
	print("Your address is " + user_address)
	split_address = user_address.split()
	# print(split_address)  # temporary instruction to verify the list
	print("Your house number is " + split_address[0]+".")
	print("Your street is " + " ".join(split_address[1:])+".")