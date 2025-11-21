from flask import Flask, request, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Clave para firmar las cookies de sesión
app.config["SECRET_KEY"] = "cambia-esta-clave"

# "Base de datos" de prueba en memoria
USERS = {
    "admin": {
        "password_hash": generate_password_hash("1234"),
        "roles": ["ADMIN", "USER"]
    },
    "usuario": {
        "password_hash": generate_password_hash("abcd"),
        "roles": ["USER"]
    }
}

def get_current_user():
    """Devuelve el usuario autenticado a partir de la sesión."""
    username = session.get("username")
    if not username:
        return None
    user = USERS.get(username)
    if not user:
        return None
    return {"username": username, "roles": user["roles"]}


@app.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "username y password son obligatorios"}), 400

    user = USERS.get(username)
    if not user or not check_password_hash(user["password_hash"], password):
        return jsonify({"error": "Credenciales inválidas"}), 401

    # Guardar datos mínimos en la sesión (cookie firmada)
    session["username"] = username

    return jsonify({
        "message": "Login correcto",
        "user": {
            "username": username,
            "roles": user["roles"]
        }
    }), 200


@app.route("/auth/me", methods=["GET"])
def me():
    user = get_current_user()
    if not user:
        return jsonify({"error": "No autenticado"}), 401
    return jsonify(user), 200


@app.route("/auth/logout", methods=["POST"])
def logout():
    session.pop("username", None)
    return jsonify({"message": "Sesión cerrada"}), 200


if __name__ == "__main__":
    app.run(debug=True)
