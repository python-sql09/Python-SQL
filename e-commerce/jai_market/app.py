from flask import Flask, render_template, request, redirect, session, url_for, jsonify, flash
import json
import os
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')

USERS_FILE = 'users.json'
PRODUCTS_FILE = 'products.json'

def load_users():
    """Load users from JSON file"""
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_users(users):
    """Save users to JSON file"""
    try:
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f, indent=2)
        return True
    except IOError:
        return False

def load_products():
    """Load products from JSON file or return default products"""
    if os.path.exists(PRODUCTS_FILE):
        try:
            with open(PRODUCTS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    
    # Default products
    return [
        {
            "id": 1, 
            "title": "Handcrafted Silver Ring", 
            "price": 45.99,
            "description": "Beautiful handmade silver ring with intricate designs",
            "stock": 10,
            "category": "jewelry"
        },
        {
            "id": 2, 
            "title": "Macrame Plant Hanger", 
            "price": 25.50,
            "description": "Eco-friendly macrame plant hanger for your home",
            "stock": 15,
            "category": "home"
        },
        {
            "id": 3, 
            "title": "Digital Art Pack", 
            "price": 15.00,
            "description": "Collection of high-quality digital artwork",
            "stock": 100,
            "category": "digital"
        },
        {
            "id": 4, 
            "title": "Wooden Coffee Mug", 
            "price": 32.00,
            "description": "Handcrafted wooden mug perfect for your morning coffee",
            "stock": 8,
            "category": "home"
        }
    ]

@app.route('/')
def home():
    return render_template('index.html', user=session.get("user"))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        email = request.form.get('email', '').strip()
        
        # Validation
        if not username or not password:
            flash('Username and password are required!', 'error')
            return render_template('signup.html')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters long!', 'error')
            return render_template('signup.html')
        
        users = load_users()
        if username in users:
            flash('Username already exists! Please choose another.', 'error')
            return render_template('signup.html')
        
        # Create new user
        users[username] = {
            "password": generate_password_hash(password),
            "email": email,
            "created_at": datetime.now().isoformat()
        }
        
        if save_users(users):
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Error creating account. Please try again.', 'error')
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        if not username or not password:
            flash('Please enter both username and password.', 'error')
            return render_template('login.html')
        
        users = load_users()
        if username in users and check_password_hash(users[username]['password'], password):
            session['user'] = username
            flash(f'Welcome back, {username}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    user = session.get('user')
    session.pop('user', None)
    if user:
        flash(f'Goodbye, {user}!', 'success')
    return redirect(url_for('home'))

@app.route('/api/products')
def get_products():
    """API endpoint to get all products"""
    try:
        products = load_products()
        return jsonify(products)
    except Exception as e:
        return jsonify({"error": "Failed to load products"}), 500

@app.route('/api/product/<int:product_id>')
def get_product(product_id):
    """API endpoint to get a single product by ID"""
    try:
        products = load_products()
        product = next((p for p in products if p['id'] == product_id), None)
        if product:
            return jsonify(product)
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": "Failed to load product"}), 500

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Create users file if it doesn't exist
    if not os.path.exists(USERS_FILE):
        save_users({})
    
    app.run(debug=True, host='0.0.0.0', port=5000)