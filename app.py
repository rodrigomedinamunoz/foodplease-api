from flask import Flask, jsonify, request

app = Flask(__name__)

USERS = {
    "admin": "1234",
    "usuario": "abcd"
}

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "FoodPlease API en ejecución..."})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username in USERS and USERS[username] == password:
        return jsonify({
            "success": True,
            "message": "Login correcto"
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Credenciales incorrectas"
        }), 401

