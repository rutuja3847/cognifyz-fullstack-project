from flask import Flask, render_template, request
import json
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# 🔁 Reverse
@app.route("/reverse", methods=["POST"])
def reverse():
    text = request.form["text"]
    reversed_text = text[::-1]

    data = {"length": len(text), "is_palindrome": int(text == reversed_text)}
    return render_template("index.html", result=reversed_text, chart_data=json.dumps(data))

# 🔍 Palindrome
@app.route("/palindrome", methods=["POST"])
def palindrome():
    text = request.form["text"]
    result = text == text[::-1]

    data = {"length": len(text), "is_palindrome": int(result)}
    return render_template("index.html", result="Palindrome" if result else "Not Palindrome", chart_data=json.dumps(data))

# ➕ Calculator
@app.route("/calculator", methods=["POST"])
def calculator():
    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    op = request.form["operator"]

    if op == "+":
        res = num1 + num2
    elif op == "-":
        res = num1 - num2
    elif op == "*":
        res = num1 * num2
    elif op == "/":
        res = num1 / num2 if num2 != 0 else "Error"
    else:
        res = "Invalid"

    return render_template("index.html", result=f"Result: {res}")

# 🔐 Password Checker
@app.route("/password", methods=["POST"])
def password():
    pwd = request.form["password"]

    strength = "Weak"
    if (len(pwd) >= 8 and
        re.search("[A-Z]", pwd) and
        re.search("[a-z]", pwd) and
        re.search("[0-9]", pwd) and
        re.search("[@#$%^&*]", pwd)):
        strength = "Strong"
    elif len(pwd) >= 6:
        strength = "Medium"

    return render_template("index.html", result=f"Password Strength: {strength}")

if __name__ == "__main__":
    app.run(debug=True)