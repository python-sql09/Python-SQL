from flask import Flask, render_template, request, redirect, session, url_for, jsonify, flash
import json
import os
import uuid
import hashlib
import hmac
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import secrets
import re

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(32))
app.permanent_session_lifetime = timedelta(days=7)

# File paths
USERS_FILE = 'data/users.json'
PRODUCTS_FILE = 'data/products.json'
ORDERS_FILE = 'data/orders.json'
STORES_FILE = 'data/stores.json'
UPLOAD_FOLDER = 'static/uploads'

# Create directories if they don't exist
os.makedirs('data', exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Utility functions
def load_json_file(filename):
    """Load JSON file with error handling"""
    if not os.path.exists(filename):
        return {}
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_json_file(filename, data):
    """Save JSON file with error handling"""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        return True
    except IOError:
        return False

def generate_order_id():
    """Generate unique order ID"""
    return f"ORD-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8].upper()}"

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def hash_payment_info(info):
    """Hash sensitive payment information"""
    return hashlib.sha256(f"{info}{app.secret_key}".encode()).hexdigest()

def require_login():
    """Check if user is logged in"""
    return session.get('user_id') is not None

def require_seller():
    """Check if user is a seller"""
    if not require_login():
        return False
    users = load_json_file(USERS_FILE)
    user = users.get(session['user_id'], {})
    return user.get('account_type') == 'seller'

# Routes
@app.route('/')
def home():
    products = load_json_file(PRODUCTS_FILE)
    featured_products = [p for p in products.values() if p.get('featured', False)][:6]
    return render_template('index.html', 
                         user=session.get('username'), 
                         user_type=session.get('user_type'),
                         featured_products=featured_products)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        account_type = request.form.get('account_type', 'buyer')
        full_name = request.form.get('full_name', '').strip()
        phone = request.form.get('phone', '').strip()
        
        # Validation
        if not all([username, email, password, full_name]):
            flash('All required fields must be filled!', 'error')
            return render_template('signup.html')
        
        if not validate_email(email):
            flash('Please enter a valid email address!', 'error')
            return render_template('signup.html')
        
        if len(password) < 8:
            flash('Password must be at least 8 characters long!', 'error')
            return render_template('signup.html')
        
        users = load_json_file(USERS_FILE)
        
        # Check if username or email already exists
        for user_id, user_data in users.items():
            if user_data.get('username') == username:
                flash('Username already exists!', 'error')
                return render_template('signup.html')
            if user_data.get('email') == email:
                flash('Email already registered!', 'error')
                return render_template('signup.html')
        
        # Create new user
        user_id = str(uuid.uuid4())
        users[user_id] = {
            "username": username,
            "email": email,
            "password": generate_password_hash(password),
            "full_name": full_name,
            "phone": phone,
            "account_type": account_type,
            "created_at": datetime.now().isoformat(),
            "verified": False,
            "profile_completed": False,
            "addresses": [],
            "payment_methods": []
        }
        
        # If seller, create store
        if account_type == 'seller':
            stores = load_json_file(STORES_FILE)
            store_id = str(uuid.uuid4())
            stores[store_id] = {
                "store_name": f"{full_name}'s Store",
                "owner_id": user_id,
                "description": "",
                "created_at": datetime.now().isoformat(),
                "status": "active"
            }
            save_json_file(STORES_FILE, stores)
            users[user_id]["store_id"] = store_id
        
        if save_json_file(USERS_FILE, users):
            flash('Account created successfully! Please complete your profile.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Error creating account. Please try again.', 'error')
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form.get('identifier', '').strip()  # username or email
        password = request.form.get('password', '')
        remember_me = request.form.get('remember_me', False)
        
        if not identifier or not password:
            flash('Please enter your credentials.', 'error')
            return render_template('login.html')
        
        users = load_json_file(USERS_FILE)
        
        # Find user by username or email
        user_id = None
        user_data = None
        for uid, data in users.items():
            if data.get('username') == identifier or data.get('email') == identifier:
                user_id = uid
                user_data = data
                break
        
        if user_data and check_password_hash(user_data['password'], password):
            session['user_id'] = user_id
            session['username'] = user_data['username']
            session['user_type'] = user_data.get('account_type', 'buyer')
            session['full_name'] = user_data.get('full_name', '')
            
            if remember_me:
                session.permanent = True
            
            flash(f'Welcome back, {user_data["full_name"]}!', 'success')
            
            # Redirect based on user type
            if user_data.get('account_type') == 'seller':
                return redirect(url_for('seller_dashboard'))
            else:
                return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    user = session.get('full_name', 'User')
    session.clear()
    flash(f'Goodbye, {user}!', 'success')
    return redirect(url_for('home'))

@app.route('/profile')
def profile():
    if not require_login():
        flash('Please log in to access your profile.', 'error')
        return redirect(url_for('login'))
    
    users = load_json_file(USERS_FILE)
    user = users.get(session['user_id'], {})
    return render_template('profile.html', user=user)

@app.route('/profile/edit', methods=['GET', 'POST'])
def edit_profile():
    if not require_login():
        flash('Please log in to edit your profile.', 'error')
        return redirect(url_for('login'))
    
    users = load_json_file(USERS_FILE)
    user = users.get(session['user_id'], {})
    
    if request.method == 'POST':
        user['full_name'] = request.form.get('full_name', '').strip()
        user['phone'] = request.form.get('phone', '').strip()
        user['bio'] = request.form.get('bio', '').strip()
        user['profile_completed'] = True
        user['updated_at'] = datetime.now().isoformat()
        
        if save_json_file(USERS_FILE, users):
            session['full_name'] = user['full_name']
            flash('Profile updated successfully!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Error updating profile.', 'error')
    
    return render_template('edit_profile.html', user=user)

@app.route('/addresses')
def addresses():
    if not require_login():
        flash('Please log in to manage addresses.', 'error')
        return redirect(url_for('login'))
    
    users = load_json_file(USERS_FILE)
    user = users.get(session['user_id'], {})
    return render_template('addresses.html', addresses=user.get('addresses', []))

@app.route('/addresses/add', methods=['GET', 'POST'])
def add_address():
    if not require_login():
        flash('Please log in to add an address.', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        address = {
            'id': str(uuid.uuid4()),
            'type': request.form.get('type', 'home'),
            'full_name': request.form.get('full_name', ''),
            'street': request.form.get('street', ''),
            'city': request.form.get('city', ''),
            'state': request.form.get('state', ''),
            'zip_code': request.form.get('zip_code', ''),
            'country': request.form.get('country', 'US'),
            'is_default': request.form.get('is_default', False) == 'on'
        }
        
        users = load_json_file(USERS_FILE)
        user = users.get(session['user_id'], {})
        
        if 'addresses' not in user:
            user['addresses'] = []
        
        # If this is default, remove default from others
        if address['is_default']:
            for addr in user['addresses']:
                addr['is_default'] = False
        
        user['addresses'].append(address)
        
        if save_json_file(USERS_FILE, users):
            flash('Address added successfully!', 'success')
            return redirect(url_for('addresses'))
        else:
            flash('Error adding address.', 'error')
    
    return render_template('add_address.html')

@app.route('/payment-methods')
def payment_methods():
    if not require_login():
        flash('Please log in to manage payment methods.', 'error')
        return redirect(url_for('login'))
    
    users = load_json_file(USERS_FILE)
    user = users.get(session['user_id'], {})
    return render_template('payment_methods.html', payment_methods=user.get('payment_methods', []))

@app.route('/payment-methods/add', methods=['GET', 'POST'])
def add_payment_method():
    if not require_login():
        flash('Please log in to add a payment method.', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        card_number = request.form.get('card_number', '').replace(' ', '')
        
        # Basic card validation
        if len(card_number) < 13 or len(card_number) > 19:
            flash('Invalid card number.', 'error')
            return render_template('add_payment_method.html')
        
        payment_method = {
            'id': str(uuid.uuid4()),
            'type': 'card',
            'card_type': request.form.get('card_type', ''),
            'last_four': card_number[-4:],
            'card_hash': hash_payment_info(card_number),  # Store hash, not actual number
            'expiry_month': request.form.get('expiry_month', ''),
            'expiry_year': request.form.get('expiry_year', ''),
            'cardholder_name': request.form.get('cardholder_name', ''),
            'is_default': request.form.get('is_default', False) == 'on',
            'added_at': datetime.now().isoformat()
        }
        
        users = load_json_file(USERS_FILE)
        user = users.get(session['user_id'], {})
        
        if 'payment_methods' not in user:
            user['payment_methods'] = []
        
        # If this is default, remove default from others
        if payment_method['is_default']:
            for method in user['payment_methods']:
                method['is_default'] = False
        
        user['payment_methods'].append(payment_method)
        
        if save_json_file(USERS_FILE, users):
            flash('Payment method added successfully!', 'success')
            return redirect(url_for('payment_methods'))
        else:
            flash('Error adding payment method.', 'error')
    
    return render_template('add_payment_method.html')

# Seller routes
@app.route('/seller/dashboard')
def seller_dashboard():
    if not require_seller():
        flash('Access denied. Seller account required.', 'error')
        return redirect(url_for('home'))
    
    products = load_json_file(PRODUCTS_FILE)
    orders = load_json_file(ORDERS_FILE)
    
    # Get seller's products and orders
    seller_products = {k: v for k, v in products.items() if v.get('seller_id') == session['user_id']}
    seller_orders = [o for o in orders.values() if any(item.get('seller_id') == session['user_id'] for item in o.get('items', []))]
    
    stats = {
        'total_products': len(seller_products),
        'total_orders': len(seller_orders),
        'revenue': sum(o.get('total', 0) for o in seller_orders if o.get('status') == 'completed'),
        'pending_orders': len([o for o in seller_orders if o.get('status') == 'pending'])
    }
    
    return render_template('seller_dashboard.html', stats=stats, recent_orders=seller_orders[:5])

@app.route('/seller/products')
def seller_products():
    if not require_seller():
        flash('Access denied. Seller account required.', 'error')
        return redirect(url_for('home'))
    
    products = load_json_file(PRODUCTS_FILE)
    seller_products = {k: v for k, v in products.items() if v.get('seller_id') == session['user_id']}
    
    return render_template('seller_products.html', products=seller_products)

@app.route('/seller/products/add', methods=['GET', 'POST'])
def add_product():
    if not require_seller():
        flash('Access denied. Seller account required.', 'error')
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        product_id = str(uuid.uuid4())
        product = {
            'id': product_id,
            'title': request.form.get('title', '').strip(),
            'description': request.form.get('description', '').strip(),
            'price': float(request.form.get('price', 0)),
            'stock': int(request.form.get('stock', 0)),
            'category': request.form.get('category', ''),
            'tags': request.form.get('tags', '').split(','),
            'seller_id': session['user_id'],
            'seller_name': session['full_name'],
            'featured': request.form.get('featured', False) == 'on',
            'status': 'active',
            'created_at': datetime.now().isoformat(),
            'images': []
        }
        
        products = load_json_file(PRODUCTS_FILE)
        products[product_id] = product
        
        if save_json_file(PRODUCTS_FILE, products):
            flash('Product added successfully!', 'success')
            return redirect(url_for('seller_products'))
        else:
            flash('Error adding product.', 'error')
    
    return render_template('add_product.html')

# Shopping and order routes
@app.route('/shop')
def shop():
    products = load_json_file(PRODUCTS_FILE)
    category = request.args.get('category', '')
    search = request.args.get('search', '')
    
    filtered_products = products.values()
    
    if category:
        filtered_products = [p for p in filtered_products if p.get('category', '').lower() == category.lower()]
    
    if search:
        filtered_products = [p for p in filtered_products if search.lower() in p.get('title', '').lower() or search.lower() in p.get('description', '').lower()]
    
    return render_template('shop.html', products=list(filtered_products), categories=['jewelry', 'home', 'digital', 'clothing', 'art'])

@app.route('/product/<product_id>')
def product_detail(product_id):
    products = load_json_file(PRODUCTS_FILE)
    product = products.get(product_id)
    
    if not product:
        flash('Product not found.', 'error')
        return redirect(url_for('shop'))
    
    return render_template('product_detail.html', product=product)

@app.route('/cart')
def cart():
    if not require_login():
        flash('Please log in to view your cart.', 'error')
        return redirect(url_for('login'))
    
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    if not require_login():
        flash('Please log in to checkout.', 'error')
        return redirect(url_for('login'))
    
    users = load_json_file(USERS_FILE)
    user = users.get(session['user_id'], {})
    
    return render_template('checkout.html', 
                         addresses=user.get('addresses', []), 
                         payment_methods=user.get('payment_methods', []))

@app.route('/orders')
def orders():
    if not require_login():
        flash('Please log in to view your orders.', 'error')
        return redirect(url_for('login'))
    
    orders = load_json_file(ORDERS_FILE)
    user_orders = [o for o in orders.values() if o.get('user_id') == session['user_id']]
    
    return render_template('orders.html', orders=user_orders)

# API routes
@app.route('/api/products')
def api_products():
    products = load_json_file(PRODUCTS_FILE)
    return jsonify(list(products.values()))

@app.route('/api/product/<product_id>')
def api_product(product_id):
    products = load_json_file(PRODUCTS_FILE)
    product = products.get(product_id)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

@app.route('/api/place-order', methods=['POST'])
def api_place_order():
    if not require_login():
        return jsonify({'error': 'Login required'}), 401
    
    data = request.get_json()
    cart_items = data.get('items', [])
    address_id = data.get('address_id')
    payment_method_id = data.get('payment_method_id')
    
    if not cart_items:
        return jsonify({'error': 'Cart is empty'}), 400
    
    # Create order
    order_id = generate_order_id()
    order = {
        'id': order_id,
        'user_id': session['user_id'],
        'items': cart_items,
        'subtotal': sum(item['price'] * item['quantity'] for item in cart_items),
        'tax': 0,  # Calculate based on location
        'shipping': 5.99,  # Flat rate for demo
        'total': sum(item['price'] * item['quantity'] for item in cart_items) + 5.99,
        'status': 'pending',
        'address_id': address_id,
        'payment_method_id': payment_method_id,
        'created_at': datetime.now().isoformat(),
        'estimated_delivery': (datetime.now() + timedelta(days=7)).isoformat()
    }
    
    orders = load_json_file(ORDERS_FILE)
    orders[order_id] = order
    
    if save_json_file(ORDERS_FILE, orders):
        return jsonify({'success': True, 'order_id': order_id})
    
    return jsonify({'error': 'Failed to place order'}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Initialize data files
    for file_path in [USERS_FILE, PRODUCTS_FILE, ORDERS_FILE, STORES_FILE]:
        if not os.path.exists(file_path):
            save_json_file(file_path, {})
    
    app.run(debug=True, host='0.0.0.0', port=5000)