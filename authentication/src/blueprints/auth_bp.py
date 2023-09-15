from flask import Blueprint


auth_blue_print = Blueprint("auth_bp", __name__, template_folder="templates")





@auth_blue_print.route("/signup")
def sign_up():
    pass