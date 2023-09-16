import hashlib
from flask import Blueprint, request

from helpers.response import Response



signup_blue_print = Blueprint("auth_bp", __name__, template_folder="templates")



@signup_blue_print.route("/signup", methods=['POST'])
def sign_up():
    data = request.get_json()

    if not data:
        return Response(
            error="Invalid data",
            status_code=400
        )
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")
    
    input_value = {
        "first_name": first_name, 
        "last_name": last_name, 
        "email": email, 
        "password": password}
   
    # Validate empty values
    if not all(input_value.values()):
        empty_value = [key for key, value in input_value.items() if  bool(value) is False]
        return Response(
            error=f"{', '.join(empty_value)} value must not empty",
            status_code=400
        )

    hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()

    # check DB for email

    return Response(data={"name": "Funso joba"})