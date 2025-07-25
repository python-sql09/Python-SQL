# -------------------------------------------------------------------------------------------
# Project Name: Burger Shop Process Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/Burger-Shop-Process
# Date        : February 1, 2025 to February 21, 2025
# Description : This is Get order from the Customer
# ---------------------------------------------------------------------------------------------------------
from menu import burger
from menu import drink
from menu import side
from menu import combo
from order import order
# 12 Defining side constants
BURGER_PRICE = 6.02
BURGER_CONDIMENTS = ["tomato", "lettuce", "onion", "cheese", "mustard", "ketchup"]
DRINK_TYPES = ["fanta", "coca cola", "sprite", "water"]
DRINK_SIZES = [12, 16, 20]
DRINK_PRICES = [1.00, 2.00, 3.00, 0.00]  # Water is free, so its price is 0.00
SIDES = ["fries", "coleslaw", "salad", "onion rings", "fruit"]
SIDE_PRICE = 3.00
COMBO_DISCOUNT = 2.00

# 9 Getting a burger order
def get_burger_order():
    b = burger("Burger", BURGER_PRICE)
    
    # Ask for condiments
    q1 = input("Do you want any condiments on your burger? (y for yes) ")
    if q1.lower() == "y":
        for condiment in BURGER_CONDIMENTS:
            q = input(f"Do you want {condiment}? (y/n): ")
            if q.lower() == "y":
                b.add_condiment(condiment)

    # Ask for extras
    q2 = input("Do you want to add cheese for $1.00? (y/n): ")
    if q2.lower() == "y":
        b.add_cheese()
    
    q3 = input("Do you want to add an extra patty for $2.00? (y/n): ")
    if q3.lower() == "y":
        b.add_extra_patty()
    
    return b

# 11 Adding a drink
def get_drink_order():
	print ("These are the available drinks:")
	print (DRINK_TYPES)
	print ("These are the available sizes:")
	print (DRINK_SIZES)
	choice = False
	drink_name = None
	drink_size = None
	drink_price = None
	while choice == False:
		q1 = input("What drink do you want? ")
		if q1.lower() in DRINK_TYPES:
			choice = True
			drink_name = q1.lower()
		else:
			print("Please enter a valid drink.")
	choice = False
	while choice == False:
		q1 = input("What size do you want? " + str(DRINK_SIZES) + ": ")
		if int(q1) in DRINK_SIZES:
			choice = True
			drink_size = int(q1)
		else:
			print("please enter a valid size")
	#locate the price of the drink based on the index of the size:
	drink_price = DRINK_PRICES[DRINK_SIZES.index(drink_size)]
	d = drink(drink_name,drink_size,drink_price)
	return d

# 13 Adding a side order
def get_side_order():
	print("These are the available sides:")
	print(SIDES)
	choice = False
	side_name = None
	while choice == False:
		q1 = input("What side do you want? ")
		if q1.lower() in SIDES:
			choice = True
			side_name = q1.lower()
		else:
			print("Please enter a valid side.")
	s = side(side_name,SIDE_PRICE)
	return s

# 15 Getting a combo
def get_combo_order():
	print("Let's get you a combo meal!")
	print("First, let's order the burger for your combo.")
	b = get_burger_order()
	print("Now, let's order the drink for your combo.")
	d = get_drink_order()
	print("Finally, let's order the side for your combo.")
	s = get_side_order()
	c = combo("Combo",b,d,s,COMBO_DISCOUNT)
	#print(str(c))
	return c

# 8 Creating an order once
def order_once():
	possible_options = [1,2,3,4]
	print("Type 1 for a Burger.")
	print("Type 2 for a Drink.")
	print("Type 3 for a Side.")
	print("Type 4 for a Combo.")
	choice = None
	while choice == None:
		q1 = input("Please enter your choice:")
		if int(q1) in possible_options:
			choice = int(q1)
	item = None
	if choice == 1:
		item = get_burger_order()
	elif choice == 2:
		item = get_drink_order()
	elif choice == 3:
		item = get_side_order()
	elif choice == 4:
		item = get_combo_order()
	return item

# 7 Creating an order
def order_many():
	print("Welcome to Deepa's Burger Shop!")
	q1 = input("May I have your name for the order? ")
	o = order(q1)
	print("Let's get your order in!")
	done = False
	while done == False:
		item = order_once()
		o.add_item(item)
		q1= input("Do you need more items? (Enter n to stop.) ")
		if q1.lower()=="n":
			done = True
	return o
client_order = order_many()
client_order.display()
