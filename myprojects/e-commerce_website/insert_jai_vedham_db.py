import sqlite3

# Connect to existing database
conn = sqlite3.connect('jai_marketplace.db')
cursor = conn.cursor()

# 1. Insert users (seller and buyer)
cursor.execute("INSERT INTO users (name, email, password_hash, role) VALUES (?, ?, ?, ?)",
               ('Alice Seller', 'alice@example.com', 'hashed_pw_123', 'seller'))

cursor.execute("INSERT INTO users (name, email, password_hash, role) VALUES (?, ?, ?, ?)",
               ('Bob Buyer', 'bob@example.com', 'hashed_pw_456', 'buyer'))

# 2. Insert product categories
categories = ['Jewelry', 'Clothing', 'Plants', 'Digital Downloads']
for cat in categories:
    cursor.execute("INSERT INTO categories (name) VALUES (?)", (cat,))

# 3. Insert products by Alice (seller_id = 1)
cursor.execute('''
INSERT INTO products (seller_id, name, description, price, stock_quantity, category_id, image_url)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', (1, 'Handmade Necklace', 'Beautiful beaded necklace.', 30.0, 5, 1, 'http://image.url/necklace.jpg'))

cursor.execute('''
INSERT INTO products (seller_id, name, description, price, stock_quantity, category_id, image_url)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', (1, 'Macrame Plant Hanger', 'Perfect for indoor plants.', 20.0, 3, 3, 'http://image.url/hanger.jpg'))

# 4. Insert an order by Bob (buyer_id = 2)
cursor.execute('''
INSERT INTO orders (buyer_id, total_amount, status)
VALUES (?, ?, ?)
''', (2, 50.0, 'pending'))

# 5. Insert order items
cursor.execute('''
INSERT INTO order_items (order_id, product_id, quantity, price)
VALUES (?, ?, ?, ?)
''', (1, 1, 1, 30.0))

cursor.execute('''
INSERT INTO order_items (order_id, product_id, quantity, price)
VALUES (?, ?, ?, ?)
''', (1, 2, 1, 20.0))

# 6. Insert a product review by Bob
cursor.execute('''
INSERT INTO reviews (product_id, buyer_id, rating, comment)
VALUES (?, ?, ?, ?)
''', (1, 2, 5, 'Loved the necklace! Great quality and fast delivery.'))

# Save changes
conn.commit()
conn.close()

print("✅ Sample data inserted into Jai Vedham Marketplace.")
