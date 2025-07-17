from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import json, os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "jai-market-secret"  # Keep this secret in production

USERS_FILE = 'users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

@app.route('/')
def home():
    return render_template('index.html', user=session.get("user"))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users:
            return "User already exists!"
        users[username] = {"password": generate_password_hash(password)}
        save_users(users)
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users and check_password_hash(users[username]['password'], password):
            session['user'] = username
            return redirect(url_for('home'))
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/api/products')
def get_products():
    products = [
        {"id": 1, "title": "Handcrafted Silver Ring", "price": 45.99},
        {"id": 2, "title": "Macrame Plant Hanger", "price": 25.50},
        {"id": 3, "title": "Digital Art Pack", "price": 15.00}
    ]
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)