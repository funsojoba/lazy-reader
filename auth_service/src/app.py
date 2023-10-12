import os
import logging
from datetime import datetime

from decouple import config
from dotenv import load_dotenv

from flask_cors import CORS, cross_origin
from flask import Flask, request
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from src.auth.route import auth_bp
from src.helpers.response import api_response


from src.db import db
from src.auth.model import User


load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["CORS_HEADERS"] = "Content-Type"


CORS(app, resources={r"/*": {"origins": "*"}})
Migrate(app, db)
jwt = JWTManager(app)
db.init_app(app)

# Routes
app.register_blueprint(auth_bp)


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    user_id = jwt_data["sub"]
    user = User.query.get(user_id)
    return user


@app.route("/")
def index():
    return api_response(
        200,
        data={
            "name": "Auth Service", 
            "date": datetime.now().strftime("%B %d, %Y")},
        message="Welcome to my API",
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0", 
        debug=True if config("ENVIRONMENT") == "development" else False, 
        port=config("PORT"), 
        threaded=False)
