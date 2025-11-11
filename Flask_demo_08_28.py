from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
#moi database
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({'message': 'User already exists'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    users[username] = hashed_password

    return jsonify({'message': f'User registered successfully: {username}'}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_jsonify()
    usernae = data.get("username")
    password = data.get("password")

    stored_pw = users.get("username")
    if stored_pw and bcrypt.check_password_hash(stored_pw, password):
        return jsonify({"message": "Login successful: {username}"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "_main_":
    app.run(debug=True)