# Exercise 4: Dogs and Cats
# Use vehicles
# Base Class
class Vehicle:
    def __init__(self, type_of_vehicle):
        self.type_of_vehicle = type_of_vehicle

    def display_info(self):
        print(f"Type of Vehicle: {self.type_of_vehicle}")

# Derived Class: Car
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

# Inherited Class 1: SUV
class SUV(Car):
    def __init__(self, type_of_vehicle, brand, model, fuel_type, year, offroad_capability):
        super().__init__(type_of_vehicle, brand, model, fuel_type, year)
        self.offroad_capability = offroad_capability  # New attribute specific to SUV

    def display_info(self):
        super().display_info()
        print(f"Offroad Capability: {self.offroad_capability}")

# Inherited Class 2: Sedan
class Sedan(Car):
    def __init__(self, type_of_vehicle, brand, model, fuel_type, year, luxury_level):
        super().__init__(type_of_vehicle, brand, model, fuel_type, year)
        self.luxury_level = luxury_level  # New attribute specific to Sedan

    def display_info(self):
        super().display_info()
        print(f"Luxury Level: {self.luxury_level}")

# Create Objects for SUV
suv1 = SUV("Car", "Jeep", "Wrangler", "Gasoline", 2022, "High")
suv2 = SUV("Car", "Land Rover", "Defender", "Diesel", 2023, "Very High")

# Create Objects for Sedan
sedan1 = Sedan("Car", "Mercedes-Benz", "E-Class", "Gasoline", 2021, "Luxury")
sedan2 = Sedan("Car", "BMW", "5 Series", "Hybrid", 2022, "High Luxury")

# Display Information for SUV Objects
print("SUV Objects:")
suv1.display_info()
print("-----------------")
suv2.display_info()

# Display Information for Sedan Objects
print("\nSedan Objects:")
sedan1.display_info()
print("-----------------")
sedan2.display_info()