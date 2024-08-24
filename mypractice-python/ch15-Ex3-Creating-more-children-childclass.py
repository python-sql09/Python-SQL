# Exercise 3: Creating More Children
# Base Class
class Vehicle:
    def __init__(self, type_of_vehicle):
        self.type_of_vehicle = type_of_vehicle

    def display_info(self):
        print(f"Type of Vehicle: {self.type_of_vehicle}")

# First Child Class: Car
class Car(Vehicle):
    def __init__(self, type_of_vehicle, brand, model, fuel_type, year):
        super().__init__(type_of_vehicle)
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Year: {self.year}")

# Second Child Class: Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, type_of_vehicle, brand, engine_capacity, type_of_bike, has_sidecar):
        super().__init__(type_of_vehicle)
        self.brand = brand
        self.engine_capacity = engine_capacity  # in cc
        self.type_of_bike = type_of_bike  # e.g., cruiser, sport, etc.
        self.has_sidecar = has_sidecar  # Boolean

    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")
        print(f"Engine Capacity: {self.engine_capacity}cc")
        print(f"Type of Bike: {self.type_of_bike}")
        print(f"Has Sidecar: {self.has_sidecar}")

# Third Child Class: Truck
class Truck(Vehicle):
    def __init__(self, type_of_vehicle, brand, capacity, wheels, has_trailer):
        super().__init__(type_of_vehicle)
        self.brand = brand
        self.capacity = capacity  # in tons
        self.wheels = wheels  # Number of wheels
        self.has_trailer = has_trailer  # Boolean

    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")
        print(f"Capacity: {self.capacity} tons")
        print(f"Wheels: {self.wheels}")
        print(f"Has Trailer: {self.has_trailer}")

# Create Car Objects
car1 = Car("Car", "Toyota", "Camry", "Gasoline", 2021)
car2 = Car("Car", "Tesla", "Model S", "Electric", 2023)

# Create Motorcycle Objects
motorcycle1 = Motorcycle("Motorcycle", "Harley-Davidson", 1200, "Cruiser", False)
motorcycle2 = Motorcycle("Motorcycle", "Ducati", 900, "Sport", False)

# Create Truck Objects
truck1 = Truck("Truck", "Volvo", 18, 10, True)
truck2 = Truck("Truck", "Ford", 5, 6, False)

# Display Information for Each Object
print("Car Objects:")
car1.display_info()
print("-----------------")
car2.display_info()
print("\nMotorcycle Objects:")
motorcycle1.display_info()
print("-----------------")
motorcycle2.display_info()
print("\nTruck Objects:")
truck1.display_info()
print("-----------------")
truck2.display_info()