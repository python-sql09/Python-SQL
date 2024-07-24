# A short python program
user_input_length = input("Enter a length (whole number): ")
user_input_width = input("Enter a width (whole number): ")
user_input_price = input("Enter a price (numbers and decimal only): ")
length = int(user_input_length)
width = int(user_input_width)
price = float(user_input_price)
# Do calculations
total_footage = length * width
total_cost = total_footage * price
# display results
print("-­-­-­-­-­-­-­-­-­-­-­-­-­-­-­-­-­")
print("Length: ", length)
print("Width: ", width)
print("Total Footage: ", total_footage)
print("Total Cost: ", total_cost)
