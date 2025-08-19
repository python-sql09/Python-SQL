from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import json, os

app = Flask(__name__)
app.secret_key = "your_secret_key_here_change_this_in_production"  # 🔐 Change this in production!
USER_FILE = "users.json"

def load_users():
    """Load users from JSON file"""
    if not os.path.exists(USER_FILE) or os.stat(USER_FILE).st_size == 0:
        return []
    try:
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_users(users):
    """Save users to JSON file"""
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=2)

def find_user_by_email(email):
    """Find user by email"""
    users = load_users()
    return next((user for user in users if user.get("email") == email), None)

@app.route("/")
def home():
    user = session.get("user")
    show_modal = session.pop("show_modal", None)
    return render_template("index.html", user=user, show_modal=show_modal)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Get form data
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        phone = request.form.get("phone", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")
        security_question = request.form.get("security_question", "")
        security_answer = request.form.get("security_answer", "").strip()

        # Validation
        if not all([username, email, phone, password, confirm_password, security_question, security_answer]):
            flash("❌ All fields are required")
            return redirect(url_for("signup"))

        if password != confirm_password:
            flash("❌ Passwords do not match")
            return redirect(url_for("signup"))

        if len(password) < 6:
            flash("❌ Password must be at least 6 characters long")
            return redirect(url_for("signup"))

        # Check if user already exists
        if find_user_by_email(email):
            flash("❌ Email already exists")
            return redirect(url_for("signup"))

        # Create new user
        users = load_users()
        new_user = {
            "id": len(users) + 1,
            "username": username,
            "email": email,
            "phone": phone,
            "password": generate_password_hash(password),  # Hash the password
            "security_question": security_question,
            "security_answer": security_answer.lower()  # Store in lowercase for comparison
        }
        
        users.append(new_user)
        save_users(users)

        flash("✅ Account created successfully! Please login.")
        session["show_modal"] = "login"
        return redirect(url_for("home"))

    return render_template("signup.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    if not email or not password:
        flash("❌ Email and password are required")
        session["show_modal"] = "login"
        return redirect(url_for("home"))

    user = find_user_by_email(email)
    
    if user and check_password_hash(user["password"], password):
        session["user"] = user["username"]
        session["user_id"] = user["id"]
        flash("✅ Login successful!")
        return redirect(url_for("home"))
    else:
        flash("❌ Invalid email or password")
        session["show_modal"] = "login"
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.clear()
    flash("👋 You've been logged out.")
    return redirect(url_for("home"))

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        answer = request.form.get("answer", "")

        if not email:
            flash("❌ Email is required")
            return redirect(url_for("forgot_password"))

        user = find_user_by_email(email)
        
        if not user:
            flash("❌ Email not found")
            return redirect(url_for("forgot_password"))

        if answer:
            # Check security answer
            if user.get("security_answer", "").lower() == answer.strip().lower():
                # In a real app, you'd send a reset email instead of showing the password
                flash(f"✅ Your password hint: {user['password'][:3]}...")
                flash("🔒 For security, consider changing your password after login")
                session["show_modal"] = "login"
                return redirect(url_for("home"))
            else:
                flash("❌ Incorrect security answer")
                return render_template("forgot_password.html", 
                                     question=get_security_question_text(user["security_question"]),
                                     email=email)
        else:
            # Show security question
            return render_template("forgot_password.html", 
                                 question=get_security_question_text(user["security_question"]),
                                 email=email)
    
    return render_template("forgot_password.html")

def get_security_question_text(question_key):
    """Get the full text of security question"""
    questions = {
        "pet": "What is your pet's name?",
        "school": "What is your primary school name?",
        "mother": "What is your mother's maiden name?",
        "city": "Which city were you born in?",
        "nickname": "What was your childhood nickname?",
        "friend": "What is your best friend's name?"
    }
    return questions.get(question_key, "Security question not found")

# API Routes for products (mock data)
@app.route("/api/products")
def api_products():
    """Mock product API endpoint"""
    products = [
        {"id": 1, "title": "Handmade Jewelry", "price": 25.99, "category": "jewelry", "image": "/static/images/jewelry.jpg", "emoji": "💎"},
        {"id": 2, "title": "Custom Art Piece", "price": 45.00, "category": "art", "image": "/static/images/art.jpg", "emoji": "🎨"},
        {"id": 3, "title": "Organic Cotton Shirt", "price": 29.99, "category": "clothing", "image": "/static/images/clothing.jpg", "emoji": "👕"},
        {"id": 4, "title": "Home Decor Item", "price": 35.50, "category": "home", "image": "/static/images/home.jpg", "emoji": "🏠"},
        {"id": 5, "title": "Ceramic Vase", "price": 40.00, "category": "home", "image": "/static/images/vase.jpg", "emoji": "🏺"},
        {"id": 6, "title": "Leather Wallet", "price": 55.00, "category": "accessories", "image": "/static/images/wallet.jpg", "emoji": "👛"}
    ]
    return jsonify(products)

@app.route("/profile")
def profile():
    """User profile page - requires login"""
    if "user" not in session:
        flash("❌ Please login to access your profile")
        session["show_modal"] = "login"
        return redirect(url_for("home"))
    
    user = find_user_by_email(session.get("user_email", ""))
    return render_template("profile.html", user=user)

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500

if __name__ == "__main__":
    # Initialize empty users file if it doesn't exist
    if not os.path.exists(USER_FILE):
        save_users([])
    
    app.run(debug=True, host="0.0.0.0", port=5000)