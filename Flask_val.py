# app.py
import os
from flask import Flask, request, jsonify, session
import bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# ---------- Configuration ----------
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-change-me")
# Secure cookie settings (set SESSION_COOKIE_SECURE=True in production with HTTPS)
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SECURE"] = False

# ---------- Simple in-memory user store (demo only) ----------
# In production: replace with a real DB (SQLite/Postgres) - shown later.
users = {}

# ---------- Rate limiter ----------
# Default limits applied app-wide (useful fallback)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],  # global safety net
    # For production, use storage_uri="redis://localhost:6379"
)

def username_key():
    """
    Key function for per-username throttling.
    If the client provides JSON with "username", use that as key,
    otherwise fallback to IP address.
    """
    try:
        data = request.get_json(silent=True) or {}
        username = data.get("username")
        if username:
            # prefix to avoid collisions with IP keys
            return f"username:{username}"
    except Exception:
        pass
    return get_remote_address()

@app.errorhandler(429)
def rate_limit_exceeded(e):
    return jsonify({"msg": "Too many requests — rate limit exceeded"}), 429

# ---------- Routes ----------
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"msg": "username and password required"}), 400

    if username in users:
        # avoid leaking other info; simple message for demo
        return jsonify({"msg": "username already exists"}), 400

    # Hash password (bcrypt generates a salt automatically)
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    # store hashed (bytes)
    users[username] = hashed
    return jsonify({"msg": "user registered successfully"}), 201

# Apply a per-username throttling of 5 attempts per 15 minutes
# plus a per-IP fallback of 20 attempts per hour.
@app.route("/login", methods=["POST"])
@limiter.limit("5 per 15 minutes", key_func=username_key)
@limiter.limit("20 per hour")
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"msg": "username and password required"}), 400

    stored_hash = users.get(username)
    # Note: bcrypt.checkpw expects bytes
    if stored_hash and bcrypt.checkpw(password.encode("utf-8"), stored_hash):
        session["user"] = username
        return jsonify({"msg": "Login successful"}), 200

    # keep response generic to avoid username enumeration
    return jsonify({"msg": "Invalid credentials"}), 401

@app.route("/protected", methods=["GET"])
def protected():
    if "user" in session:
        return jsonify({"msg": f"Welcome {session['user']}!"}), 200
    return jsonify({"msg": "Unauthorized"}), 401

if __name__ == "__main__":
    # debug=True is OK for local dev, but disable in production
    app.run(debug=True)
