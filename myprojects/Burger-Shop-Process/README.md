Date:
February 1, 2025 to February 21, 2025

REQUIREMENTS FOR OUR BURGER SHOP APPLICATION:
---------------------------------------------
Our burger shop application allows customers to place custom orders for hamburgers and other items. Within the ordering process, we will want the customer to be able to specify what kind of food or drink they want, then we’ll need to calculate the cost of the order and display the completed order to the user. More specifically, the completed application must be able to perform the following steps:
•• Ask the customer if they want a burger, a side, a drink, or a combo.
•• A combo must include a burger, a side, and a drink.
•• Prompt them for details about their selection, such as condiments for a burger, what kind and size of drink, and so on.
•• Create the item based on their selections.
•• Add the item to the order.
•• Repeat these steps until the customer doesn’t want to order anything else.
•• Display the order details including the price.
•• Thank the customer for their business.
•• Give the customer the option to cancel their order at any point in the ordering process.

PLAN THE CODE:
--------------
As a first step in any development process, we start by planning what needs to be coded in our application. This step of planning can include flowcharts or other diagrams to help visualize how the program will be structured and what it will do. We’ll start with the big picture here and then focus on smaller parts of the program as we work through the steps.

                                  Customer 
                                  enter the 
                                  restaurant
                                      |
                                      |
                                      V
                                Ask customer: 
                                Burger, Side, 
                                Drink, or Combo?
                                      |
                                      |
                                      V
                Yes  <------    Does the customer  ------> No
                 |              want combo?                |
                 |                                         | <----------------
                 V                                         V                 |
            Combo order                              Single order            |
            Burger, Side                             Burger or Side          |
            Drink size                               or Drink                |
                 |------------------>|<--------------------|                 |
                 |<--------          |          ---------->|                 |
                 V        |          |          |          V                 |
         Add item to order|          |          |   Add item to order        |
                 |        |          |          |          |                 |
                 |        |          |          |          |                 |
                 |        |No        V        No|            V             Yes |
                 |        ---Does customer ------   Does customer want  ------ 
                 |           want to cancel         more items?
                 |           the order                     |
                 |                |                        | No
                 |                | Yes                    |
                 |                |                        |
                 ---------------> |                        |
                                  | <-----------------------    
                                  V
                                 Stop
                                 


The main program itself must include the following steps:
1. Greet the customer and ask their name.
2. Ask the customer what they want to order (one item at a time!).
3. Ask the customer for customizations, such as burger toppings or drink size.
4. Add each item to the order as it is requested.
5. Ask the customer to continue or complete their order after each item.
6. When the customer completes the order, the program will display the order and the total price for the order.
The customer should be able to order any combination of the following items:
•• Burger
•• Drink
•• Side
We also want to allow them to order a combo that includes a burger, a drink, and a side at a discount.

CREATE THE CLASSES:
--------------------------------
Looking at this from an object-­oriented programming approach, we can identify multiple objects in this scenario. These include:
•• The order itself
•• The items the customer can order, which we know to be:
•• Burger
•• Drink
•• Side
•• Combo
We can define the order itself as a class. We can also define each of the items that can be ordered as a class. We can then use these classes in the main program to stream-line the code.
We can start with the classes themselves, including the classes we’ve already identified:
•• order
•• burger
•• drink
•• side
•• combo

CREATE THE FOOD ITEM CLASS:
-----------------------------
All the items on our burger shop menu have two properties in common: the name of the item and a price. This means that we can create a parent class that references those properties first, and then create child classes for the individual menu items and their specific properties. Add a new food_item class to the menu.py file 

# 1.The food_item class
class food_item:
	def __init__(self,name,price):
		self.name = name
		self.price = price
	def __str__(self):
		return "Item: " + self.name + "\n" + "Price: $" + str(self.price) + "\n"
	def get_price(self):
		return self.price
   
Create a Burger Class:
----------------------
We can reuse the food_item class to derive the burger class using inheritance. In our case, we will also track the condiments of the burger. To do that, we will add another attribute to the burger (besides name and price inherited from food_item), which we will call condiments. This attribute will track the list of condiments we want in the burger. For our case, we can use a simple list to store the condiments. The burger class is presented in Listing 2. You can add this into your menu.py file that already contains the food_item class.

# 2.The Burger class
class burger(food_item):
	def __init__(self,name,price):
		super(burger, self).__init__(name,price)
		self.condiments = []
	def add_condiment(self,condiment):
		if condiment not in self.condiments:
			self.condiments.append(condiment)
	def __str__(self):
		s = super(burger, self).__str__()
		s = s + "Condiments:" + ", ".join(self.condiments)
		return s        

