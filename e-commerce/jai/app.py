from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask import get_flashed_messages
import json, os

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # 🔐 Replace with a long, random string!
USER_FILE = "users.json"

def load_users():
    if not os.path.exists(USER_FILE) or os.stat(USER_FILE).st_size == 0:
        return []
    with open(USER_FILE) as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=2)

@app.route("/")
def home():
    user = session.get("user")
    show_modal = session.pop("show", None)
    return render_template("index.html", user=user, show_modal=show_modal)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]
        confirm = request.form["confirm_password"]
        question = request.form["security_question"]
        answer = request.form["security_answer"]

        if password != confirm:
            flash("❌ Passwords do not match")
            return redirect(url_for("signup"))

        try:
            with open("users.json", "r") as f:
                users = json.load(f)
        except:
            users = []

        if any(user["email"] == email for user in users):
            flash("❌ Email already exists")
            return redirect(url_for("signup"))

        users.append({
            "username": username,
            "email": email,
            "phone": phone,
            "password": password,
            "question": question,
            "answer": answer
        })

        with open("users.json", "w") as f:
            json.dump(users, f, indent=2)

        flash("✅ Account created. Please login.")
        return redirect(url_for("home"))

    return render_template("signup.html")

@app.route("/login", methods=["POST"])
def login():
    users = load_users()
    data = request.form

    user = next((u for u in users if u["email"] == data["email"]), None)
    if user and check_password_hash(user["password"], data["password"]):
        session["user"] = user["username"]
        flash("✅ Login successful!")
        return redirect(url_for("home"))
    else:
        flash("❌ Invalid login")
        session["show"] = "login"
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("👋 You’ve been logged out.")
    return redirect(url_for("home"))

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email")
        answer = request.form.get("answer")

        try:
            with open("users.json", "r") as f:
                users = json.load(f)
        except:
            flash("❌ No user data found.")
            return redirect(url_for("forgot_password"))

        user = next((u for u in users if u["email"] == email), None)

        if not user:
            flash("❌ Email not found.")
            return redirect(url_for("forgot_password"))

        if answer:
            if user.get("answer", "").strip().lower() == answer.strip().lower():
                return render_template("forgot_password.html", password=user["password"])
            else:
                flash("❌ Incorrect answer.")
                return redirect(url_for("forgot_password"))
        else:
            questions = {
                "pet": "What is your pet's name?",
                "school": "What is your primary school name?",
                "mother": "What is your mother's maiden name?",
                "city": "Which city were you born in?",
                "nickname": "What was your childhood nickname?",
                "friend": "What is your best friend’s name?"
            }
            return render_template("forgot_password.html", question=questions.get(user["question"]))
    
    return render_template("forgot_password.html")

if __name__ == "__main__":
    app.run(debug=True)