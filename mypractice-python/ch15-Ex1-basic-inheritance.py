# Exercise 1: Basic Inheritance
# Base Class
class Vehicle:
    def __init__(self, type_of_vehicle):
        self.type_of_vehicle = type_of_vehicle

    def display_info(self):
        print(f"Type of Vehicle: {self.type_of_vehicle}")

# Derived Class
class Car(Vehicle):
    def __init__(self, type_of_vehicle, brand, model):
        # Call the constructor of the base class
        super().__init__(type_of_vehicle)
        self.brand = brand
        self.model = model

    def display_info(self):
        # Call the display_info method of the base class
        super().display_info()
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

# Create Objects
car1 = Car("Car", "Toyota", "Camry")
car2 = Car("Car", "Tesla", "Model S")

# Display Information for Each Object
car1.display_info()
print("-----------------")
car2.display_info()