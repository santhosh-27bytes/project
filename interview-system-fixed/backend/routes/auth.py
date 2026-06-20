from flask import Blueprint
from flask import request
from flask import jsonify

auth_bp = Blueprint(
    "auth",
    __name__
)

@auth_bp.route(
    "/register",
    methods=["POST"]
)
def register():

    data = request.json or {}

    if not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email and password are required"}), 400

    return jsonify({

        "message":
        "Registration Successful",

        "user": data

    })


@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():

    data = request.json or {}

    if not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email and password are required"}), 400

    return jsonify({

        "message":
        "Login Successful"

    })
