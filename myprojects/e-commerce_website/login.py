import sqlite3
import getpass

# Connect to SQLite database
conn = sqlite3.connect('jai_marketplace.db')
cursor = conn.cursor()

# Prompt user for email and password
email = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")  # hide password input

# Query the user by email
cursor.execute("SELECT user_id, name, role, password_hash FROM users WHERE email = ?", (email,))
user = cursor.fetchone()

if user:
    user_id, name, role, stored_password = user
    if password == stored_password:
        print(f"\n✅ Login successful! Welcome, {name} ({role}).")
    else:
        print("\n❌ Incorrect password.")
else:
    print("\n❌ No user found with that email.")