from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Permite llamadas desde Flutter Web

# Usuario en duro
USER = {
    "username": "admin",
    "password": "1234"
}

# Productos en duro (platos)
PLATOS = {
    {"id": 1, "name": "Cazuela de Pollo", "price": 5990},
    {"id": 2, "name": "Empanada de Pino", "price": 1990},
    {"id": 3, "name": "Pastel de Choclo", "price": 7990},
    {"id": 4, "name": "Lomo a lo Pobre", "price": 8990},
    {"id": 5, "name": "Completo Italiano", "price": 1990},
    {"id": 6, "name": "Bebida 350 cc", "price": 1490},
    {"id": 7, "name": "Papas Fritas Familiar", "price": 4990}
}

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "FoodPlease API en ejecución..."})

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    if not data:
        return jsonify({"success": False, "message": "No se proporcionaron datos"}), 400

    if data.get("username") == USER["username"] and data.get("password") == USER["password"]:
        return jsonify({"success": True, "message": "Inicio de sesión exitoso"})

    return jsonify({"success": False, "message": "Credenciales inválidas"}), 401

@app.route("/platos", methods=["GET"])
def products():
    return jsonify(PLATOS)

if __name__ == "__main__":
    app.run(debug=True)

