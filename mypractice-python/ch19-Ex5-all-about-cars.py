import csv
from functools import reduce

def read_car_data(file_path):
    data = []
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def filter_by_make(data, make):
    return list(filter(lambda car: car['Make'].lower() == make.lower(), data))

def filter_fuel_efficient(data):
    return list(filter(lambda car: float(car['City MPG']) > 35, data))

def filter_high_horsepower(data):
    return list(filter(lambda car: float(car['Horsepower']) > 100, data))

def cost_to_drive_100_miles(data, gasoline_cost_per_gallon):
    def compute_cost(car):
        city_mpg = float(car['City MPG'])
        cost_per_mile = gasoline_cost_per_gallon / city_mpg
        return cost_per_mile * 100

    return list(map(lambda car: (car['Make'], car['Model'], compute_cost(car)), data))

def average_mpg(data):
    city_mpgs = list(map(lambda car: float(car['City MPG']), data))
    highway_mpgs = list(map(lambda car: float(car['Highway MPG']), data))
    
    avg_city_mpg = reduce(lambda x, y: x + y, city_mpgs) / len(city_mpgs)
    avg_highway_mpg = reduce(lambda x, y: x + y, highway_mpgs) / len(highway_mpgs)
    
    return avg_city_mpg, avg_highway_mpg

def average_cost(data):
    costs = list(map(lambda car: float(car['Cost']), data))
    return reduce(lambda x, y: x + y, costs) / len(costs)

def main():
    file_path = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/car_data.csv'
    data = read_car_data(file_path)

    # Filter by make
    make = input("Enter the make of the car to filter by: ")
    cars_by_make = filter_by_make(data, make)
    print(f"\nCars by {make}:")
    for car in cars_by_make:
        print(car)

    # Filter fuel-efficient cars
    fuel_efficient_cars = filter_fuel_efficient(data)
    print("\nFuel-efficient cars:")
    for car in fuel_efficient_cars:
        print(car)

    # Filter high horsepower cars
    high_horsepower_cars = filter_high_horsepower(data)
    print("\nCars with high horsepower:")
    for car in high_horsepower_cars:
        print(car)

    # Compute cost to drive 100 miles
    gasoline_cost_per_gallon = float(input("\nEnter the current gasoline cost per gallon: "))
    driving_costs = cost_to_drive_100_miles(data, gasoline_cost_per_gallon)
    print("\nCost to drive 100 miles:")
    for make, model, cost in driving_costs:
        print(f"{make} {model}: ${cost:.2f}")

    # Calculate average MPG and cost
    avg_city_mpg, avg_highway_mpg = average_mpg(data)
    avg_cost = average_cost(data)
    print(f"\nAverage city MPG: {avg_city_mpg:.2f}")
    print(f"Average highway MPG: {avg_highway_mpg:.2f}")
    print(f"Average cost of all cars: ${avg_cost:.2f}")

if __name__ == "__main__":
    main()