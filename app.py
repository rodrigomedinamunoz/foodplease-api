from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# CORS explícito para todos los endpoints
CORS(app, resources={r"/*": {"origins": "*"}})

USERS = {
    "admin": "1234",
    "usuario": "abcd"
}

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "FoodPlease API en ejecución..."})


@app.route("/login", methods=["POST", "OPTIONS"])
def login():
    # RESPUESTA AL PREFLIGHT
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200

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


@app.route("/platos", methods=["GET"])
def platos():
    return jsonify([
        {"id": 1, "name": "Cazuela de Pollo", "price": 5990},
        {"id": 2, "name": "Empanada de Pino", "price": 1990},
        {"id": 3, "name": "Pastel de Choclo", "price": 7990},
        {"id": 4, "name": "Lomo a lo Pobre", "price": 8990},
        {"id": 5, "name": "Completo Italiano", "price": 1990},
        {"id": 6, "name": "Bebida 350 cc", "price": 1490},
        {"id": 7, "name": "Papas Fritas Familiar", "price": 4990},
    ])
