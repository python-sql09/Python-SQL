# -----------------------------------------------------------------------------------------------------
# Project Name: Burger Shop Process Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/Burger-Shop-Process
# Date        : February 1, 2025 to February 21, 2025
# Description : This is Get order from the Customer
# ---------------------------------------------------------------------------------------------------------
from menu import burger, drink, side, combo
from order import order

# Constants for the menu
BURGER_PRICE = 6.00
BURGER_CONDIMENTS = ["tomato", "lettuce", "onion", "cheese", "mustard", "ketchup"]
DRINK_TYPES = ["fanta", "coca cola", "sprite", "water"]
DRINK_SIZES = [12, 16, 20]
DRINK_PRICES = [1.00, 2.00, 3.00, 0.00]  # Water is free
SIDES = ["fries", "coleslaw", "salad", "onion rings", "fruit"]
SIDE_PRICE = 3.00
COMBO_DISCOUNT = 2.00

# Function to order a burger
def get_burger_order():
    b = burger("Burger", BURGER_PRICE)
    q1 = input("Do you want any condiments on your burger? (y for yes): ")
    if q1.lower() == "y":
        for condiment in BURGER_CONDIMENTS:
            q = input(f"Do you want {condiment}? (y/n): ")
            if q.lower() == "y":
                b.add_condiment(condiment)
    q2 = input("Do you want to add cheese for $1.00? (y/n): ")
    if q2.lower() == "y":
        b.add_cheese()
    q3 = input("Do you want to add an extra patty for $2.00? (y/n): ")
    if q3.lower() == "y":
        b.add_extra_patty()
    return b

# Function to order a drink
def get_drink_order():
    print("Available drinks:", DRINK_TYPES)
    print("Available sizes:", DRINK_SIZES)
    drink_name = input("What drink do you want? ").lower()
    while drink_name not in DRINK_TYPES:
        drink_name = input("Please enter a valid drink: ").lower()
    drink_size = int(input(f"What size do you want? {DRINK_SIZES}: "))
    while drink_size not in DRINK_SIZES:
        drink_size = int(input(f"Please enter a valid size: {DRINK_SIZES}: "))
    drink_price = DRINK_PRICES[DRINK_SIZES.index(drink_size)]
    d = drink(drink_name, drink_size, drink_price)
    return d

# Function to order a side
def get_side_order():
    print("Available sides:", SIDES)
    side_name = input("What side do you want? ").lower()
    while side_name not in SIDES:
        side_name = input("Please enter a valid side: ").lower()
    s = side(side_name, SIDE_PRICE)
    return s

# Function to order a combo
def get_combo_order():
    print("Let's get you a combo meal!")
    b = get_burger_order()
    d = get_drink_order()
    s = get_side_order()
    c = combo("Combo", b, d, s, COMBO_DISCOUNT)
    return c

# Function to handle individual item orders
def order_once():
    possible_options = [1, 2, 3, 4]
    print("1. Burger\n2. Drink\n3. Side\n4. Combo")
    choice = int(input("Please enter your choice: "))
    while choice not in possible_options:
        choice = int(input("Please enter a valid choice (1-4): "))
    if choice == 1:
        return get_burger_order()
    elif choice == 2:
        return get_drink_order()
    elif choice == 3:
        return get_side_order()
    elif choice == 4:
        return get_combo_order()

# Main function to handle multiple orders
def order_many():
    print("Welcome to Deepa's Burger Shop!")
    customer_name = input("May I have your name for the order? ")
    o = order(customer_name)
    done = False
    while not done:
        item = order_once()
        o.add_item(item)
        more_items = input("Do you need more items? (Enter 'n' to stop): ")
        if more_items.lower() == 'n':
            done = True
    o.choose_payment_method()
    # Check payment method and handle card validation
    if o.payment_method == "Credit Card":
        card_balance = float(input("Enter your card balance: "))
        if card_balance < o.get_price():
            print("Insufficient funds on your card. Please choose another payment method.")
            o.choose_payment_method()
    o.display()
    o.save_transaction()

client_order = order_many()