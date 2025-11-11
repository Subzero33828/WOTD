#08/12/2025
from flask import Flask
# Flask application to demonstrate basic routing
# This application has two routes: one for a simple greeting and another that takes a name as a parameter.
# To run this application, save it as Flaskdemo.py and execute it in a Python environment

app = Flask(__name__)

@app.route("/Hello")
def hello():
    return "Hello, World!"

@app.route("/Greet/<name>")
def Greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request

# =========================
# Flask “Hello World” API
# =========================
# Demonstrates basic REST API concepts: routing, HTTP GET, and query parameters
# Run this app with: python Flaskdemo.py
# Visit in browser: 
#   - http://127.0.0.1:5000/hello
#   - http://127.0.0.1:5000/greet/YourName
#   - http://127.0.0.1:5000/greet?name=YourName

app = Flask(__name__)

# -------------------------
# Route 1: Simple greeting
# -------------------------
@app.route("/hello", methods=["GET"])
def hello():
    """
    Responds with a simple greeting.
    Example: GET /hello -> "Hello, World!"
    """
    return "Hello, World!"

# -------------------------
# Route 2: Greeting via path variable
# -------------------------
@app.route("/greet/<name>", methods=["GET"])
def greet_path(name):
    """
    Greets a user by name using a URL path variable.
    Example: GET /greet/Tyler -> "Hello, Tyler!"
    """
    return f"Hello, {name}!"

# -------------------------
# Route 3: Greeting via query parameter
# -------------------------
@app.route("/greet", methods=["GET"])
def greet_query():
    """
    Greets a user by name using a query parameter.
    If no name is provided, defaults to 'Friend'.
    Example: GET /greet?name=Tyler -> "Hello, Tyler!"
             GET /greet -> "Hello, Friend!"
    """
    # Get the 'name' parameter from the query string; default to "Friend" if missing
    name = request.args.get("name", "Friend")
    return f"Hello, {name}!"

# =========================
# Main method to run Flask app
# =========================
if __name__ == "__main__":
    # debug=True enables hot reload for development
    app.run(debug=True)
