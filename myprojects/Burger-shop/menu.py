# 10 Defining drink constants
BURGER_PRICE = 6.00
BURGER_CONDIMENTS = ["tomato", "lettuce", "onion", "cheese", "mustard", "ketchup"]
DRINK_TYPES = ["fanta", "coca cola", "sprite", "water"]
DRINK_SIZES = [12, 16, 20]
DRINK_PRICES = [1.00, 2.00, 3.00, 0.00]  # Water is free, so its price is 0.00

# 1.The food_item class
class food_item:
	def __init__(self,name,price):
		self.name = name
		self.price = price
	def __str__(self):
		return "Item: " + self.name + "\n" + "Price: $" + str(self.price) + "\n"
	def get_price(self):
		return self.price
#2 The burger class
class burger(food_item):
    def __init__(self, name, price):
        super(burger, self).__init__(name, price)
        self.condiments = []
        self.extras = []

    def add_condiment(self, condiment):
        if condiment not in self.condiments:
            self.condiments.append(condiment)

    def add_cheese(self):
        self.extras.append("cheese")
        self.price += 1.00  # Adding cheese increases price by $1.00

    def add_extra_patty(self):
        self.extras.append("extra patty")
        self.price += 2.00  # Adding extra patty increases price by $2.00

    def __str__(self):
        s = super(burger, self).__str__()
        s += "Condiments: " + ", ".join(self.condiments) + "\n"
        s += "Extras: " + ", ".join(self.extras) + "\n"
        return s
	
# 3 The drink class
class drink(food_item):
    def __init__(self,name,size,price):
        super(drink, self).__init__(name,price)
        self.size= size
    def __str__(self):
        s = super(drink, self).__str__()
        s = s + "Size: " + str(self.size) + "oz"
        return s
# 4 The side class
class side(food_item):
	def __init__(self,name,price):
		super(side, self).__init__(name, price)
# 5 The combo class
class combo(food_item):
	def __init__(self,name,b,d,s,discount):
		self.name = name
		self.burger = b
		self.drink = d
		self.side = s
		self.discount = discount
		self.price = self.burger.get_price() + self.drink.get_price() + self.side.get_price() - self.discount
	def __str__(self):
		s = ""
		s = s + "Combo: " + self.name + "\n"
		s = s + str(self.burger) + "\n" + str(self.drink)+ "\n" + str(self.side)+ "\n"
		s = s + "Combo Price Before Discount: $" + str(self.burger.get_price() + self.drink.get_price() + self.side.get_price()) + "\n"
		s = s + "Discount: $" + str(self.discount)+ "\n"
		s = s + "Combo Price After Discount: $" + str(self.price)+ "\n"
		return s