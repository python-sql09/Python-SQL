purchase_total = 0
products_to_buy = True  # Initialize this to start the loop

# Function to simulate scanning a product and returning its price
def upc_scan():
    # For simplicity, return a fixed price; in practice, this would return different prices
    return float(input("Please enter the product price (enter 0 to finish): "))

while products_to_buy:
    product_price = upc_scan()
    if product_price == 0:
        products_to_buy = False  # Stop the loop if the user enters 0
    else:
        purchase_total += product_price
        print(f"Current total: {purchase_total}")

print(f"Final total: {purchase_total}")