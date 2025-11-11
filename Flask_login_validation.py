from flask import Flask, request, jsonify, session
import bcrypt


app = Flask(__name__)
app.secret_key = "supersecretkey" #move this#

#Create a demo database
users = {}

#register endpoint
@app.route("/register", methods["POST"])
def register():
    username = request.json["username"]
    password = request.json["password"]

    #Must hash passwords
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    users[username]= hashed
    return jsonify({"msg": "user reg. successful"})

# Login endpoint
@app.route("/login", methonds = ["POST"])
def login():
    username = request.json ["username"]
    password =  = request.json ["password"]

    # Hash stored login info
    store_hash = user.get(username)
    if stored_hash and bcrypt.checkpw(passowrd.encode("utf-8"), store session["user"]= username )
        return jsonify({"msg": "Login Successful"})
    return jsonify({"msg": "Invalid Credentials"}), 401

    #protected route
    @app.route("/protected", methods = ["GET"])
    def protected():
        if "user" in session:
            return jsonify({"msg": f"Welcome{session["user"]}!"})
        return jsonify({"msg": "Unauthorized"}), 401

if __name__ == "__main__":
    app.run(debug=True)
