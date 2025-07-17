import sqlite3

# Connect to the database
conn = sqlite3.connect('jai_marketplace.db')
cursor = conn.cursor()

# 1. View all users
print("\n🧑 USERS")
cursor.execute("SELECT user_id, name, email, role FROM users")
for row in cursor.fetchall():
    print(row)

# 2. View all categories
print("\n📦 CATEGORIES")
cursor.execute("SELECT * FROM categories")
for row in cursor.fetchall():
    print(row)

# 3. View all products
print("\n🛍️ PRODUCTS")
cursor.execute('''
SELECT products.product_id, products.name, price, stock_quantity, users.name AS seller, categories.name AS category
FROM products
JOIN users ON products.seller_id = users.user_id
JOIN categories ON products.category_id = categories.category_id
''')
for row in cursor.fetchall():
    print(row)

# 4. View all orders
print("\n🧾 ORDERS")
cursor.execute('''
SELECT orders.order_id, users.name AS buyer, total_amount, status
FROM orders
JOIN users ON orders.buyer_id = users.user_id
''')
for row in cursor.fetchall():
    print(row)

# 5. View all reviews
print("\n🌟 REVIEWS")
cursor.execute('''
SELECT reviews.review_id, users.name AS buyer, products.name AS product, rating, comment
FROM reviews
JOIN users ON reviews.buyer_id = users.user_id
JOIN products ON reviews.product_id = products.product_id
''')
for row in cursor.fetchall():
    print(row)

conn.close()