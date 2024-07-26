# Define the street address
address = "25 Main Street"
# Display the full address
print(f"The full address is: {address}")
# Split the address into its components
address_parts = address.split(' ', 1)
house_number = address_parts[0]
street_name = address_parts[1]
# Display the house number
print(f"The building or house number is {house_number}.")
# Display the street name
print(f"The street name is {street_name}.")