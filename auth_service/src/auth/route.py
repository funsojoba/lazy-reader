from flask import Blueprint
from flask_cors import cross_origin, CORS


auth_bp = Blueprint("auth", __name__)
CORS(auth_bp, resources={f"/api/*": {"origin": "*"}})

# Define routes
@auth_bp.route("/api/auth/register", methods=["POST"])
@cross_origin()
def signup_function():
    from src.auth.controller import signup

    return signup()


@auth_bp.route("/api/auth/login", methods=["POST"])
@cross_origin()
def login_function():
    from src.auth.controller import login

    return login()


@auth_bp.route("/api/auth/username/set", methods=["POST"])
@cross_origin()
def set_username_function():
    from src.auth.controller import set_username

    return set_username()
