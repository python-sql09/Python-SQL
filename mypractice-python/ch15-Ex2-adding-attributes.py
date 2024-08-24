# Exercise 2: Adding Attributes
# Base Class
class Vehicle:
    def __init__(self, type_of_vehicle):
        self.type_of_vehicle = type_of_vehicle

    def display_info(self):
        print(f"Type of Vehicle: {self.type_of_vehicle}")

# Derived Class with Added Attributes
class Car(Vehicle):
    def __init__(self, type_of_vehicle, brand, model, fuel_type, year):
        # Call the constructor of the base class
        super().__init__(type_of_vehicle)
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type  # New attribute
        self.year = year  # New attribute

    def display_info(self):
        # Call the display_info method of the base class
        super().display_info()
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Year: {self.year}")

# Create Objects with New Attributes
car1 = Car("Car", "Toyota", "Camry", "Gasoline", 2021)
car2 = Car("Car", "Tesla", "Model S", "Electric", 2023)

# Display Information for Each Object
car1.display_info()
print("-----------------")
car2.display_info()