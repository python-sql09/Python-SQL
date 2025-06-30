# -------------------------------------------------------------------------------------------
# Project Name: Burger Shop Process Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/Burger-Shop-Process
# Date        : February 1, 2025 to February 21, 2025
# Description : This is Menu For the Customer
# ---------------------------------------------------------------------------------------------------------
# Menu items and constants
# Base class for food items
class food_item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Item: {self.name}\nPrice: ${self.price:.2f}\n"

    def get_price(self):
        return self.price

# Burger class
class burger(food_item):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.condiments = []
        self.extras = []

    def add_condiment(self, condiment):
        if condiment not in self.condiments:
            self.condiments.append(condiment)

    def add_cheese(self):
        self.extras.append("cheese")
        self.price += 1.00

    def add_extra_patty(self):
        self.extras.append("extra patty")
        self.price += 2.00

    def __str__(self):
        s = super().__str__()
        s += f"Condiments: {', '.join(self.condiments)}\n"
        s += f"Extras: {', '.join(self.extras)}\n"
        return s

# Drink class
class drink(food_item):
    def __init__(self, name, size, price):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        s = super().__str__()
        s += f"Size: {self.size}oz"
        return s

# Side class
class side(food_item):
    pass

# Combo class
class combo(food_item):
    def __init__(self, name, b, d, s, discount):
        self.name = name
        self.burger = b
        self.drink = d
        self.side = s
        self.discount = discount
        self.price = self.burger.get_price() + self.drink.get_price() + self.side.get_price() - self.discount

    def __str__(self):
        s = f"Combo: {self.name}\n"
        s += str(self.burger) + "\n"
        s += str(self.drink) + "\n"
        s += str(self.side) + "\n"
        s += f"Combo Price Before Discount: ${self.burger.get_price() + self.drink.get_price() + self.side.get_price():.2f}\n"
        s += f"Discount: ${self.discount:.2f}\n"
        s += f"Combo Price After Discount: ${self.price:.2f}\n"
        return s