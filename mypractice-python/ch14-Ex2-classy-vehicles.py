# Exercise 2: Classy Vehicles
class Vehicle:
    def __init__(self, vehicle_type, year, color, number_of_doors):
        self.vehicle_type = vehicle_type
        self.year = year
        self.color = color
        self.number_of_doors = number_of_doors
    
    def display(self):
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Number of Doors: {self.number_of_doors}")
    
    def has_wheels(self):
        if self.vehicle_type in ["Car", "Motorcycle", "Truck", "Bicycle"]:
            return True
        else:
            return False

# Create instances of the Vehicle class
car = Vehicle("Car", 2022, "Red", 4)
motorcycle = Vehicle("Motorcycle", 2020, "Black", 0)
boat = Vehicle("Boat", 2018, "White", 0)
bicycle = Vehicle("Bicycle", 2021, "Blue", 0)

# Display vehicle details and check if they have wheels
vehicles = [car, motorcycle, boat, bicycle]
for vehicle in vehicles:
    vehicle.display()
    print("Has Wheels:", vehicle.has_wheels())
    print()  # Add a line break between vehicle details