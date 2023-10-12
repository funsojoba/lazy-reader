from flask import request, Blueprint
from flask_jwt_extended import create_access_token

from datetime import timedelta, datetime

from marshmallow.exceptions import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash

from src.db import db
from src.auth.model import User
from src.auth.schema import UserSchema, UsernameSchema, LoginSchema, SetUsernameSchema
from src.helpers.response import api_response


def signup():
    data = request.get_json()

    user_schema = UserSchema()
    try:
        user_data = user_schema.load(data)
    except ValidationError as e:
        return api_response(400, message="Validation error", errors=e.messages)

    user_with_email = User.query.filter_by(email=user_data["email"]).all()

    if user_with_email:
        return api_response(409, message="Username already exists")

    user_data["password"] = generate_password_hash(user_data["password"])

    user = User(**user_data)
    db.session.add(user)
    db.session.commit()

    return api_response(201, message="sign up successful")


def login():
    data = request.get_json()

    user_schema = LoginSchema()
    try:
        user_data = user_schema.load(data)
    except ValidationError as e:
        return api_response(400, message="Validation error", errors=e.messages)

    user = User.query.filter_by(email=user_data["email"]).first()
    if not user:
        return api_response(404, message="User not found")

    if check_password_hash(user.password, user_data["password"]):
        access_token = create_access_token(
            identity=user.id, expires_delta=timedelta(days=1)
        )
    else:
        return api_response(401, message="Invalid credentials")

    return api_response(200, message="login successful", data=dict(token=access_token))



def generate_username(data):
    """This function generates a list of usernames from the first and last name provided in the data

    Args:
        data (_type_): dict

    Returns:
        _type_: List[str]
    """
    first_name, last_name = data.get("first_name"), data.get("last_name")
    
    additional_symbols = "0123456789_"
    usernames = []
    for i in range(8):
        first_letter = first_name[0:i+1]
        last_letter = last_name[0:len(last_name)-i]
        first_and_last_name = f"@{first_letter}{last_letter}"
        username = first_and_last_name + "".join(random.choices(additional_symbols, k=8 - len(first_and_last_name)))
        usernames.append(username)
    return usernames


def get_username():
    data = request.get_json()
    username_schema = UsernameSchema()
    try:
        user_data = username_schema.load(data)
    except ValidationError as e:
        return api_response(400, message="Validation error", errors=e.messages)

    usernames = generate_username(user_data)
    return api_response(200, message="username generated successful", data=dict(usernames=usernames))



def set_username():
    data = request.get_json()
    username = SetUsernameSchema()
    try:
        user_data = username_schema.load(data)
    except ValidationError as e:
        return api_response(400, message="Validation error", errors=e.messages)
    existing_username = User.query.filter_by(username=user_data['username']).first()
    
    if existing_username:
        return api_response(409, message="Username already exists")

    user = User.query.filter_by(email=user_data['email']).first()

    if not user:
        return api_response(404, message="User not found")
    
    user.username = user_data['username']
    db.session.commit()
    return api_response(200, message="Username set successfully")

    

