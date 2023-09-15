from flask import Blueprint

from helpers.response import Response



auth_blue_print = Blueprint("auth_bp", __name__, template_folder="templates")



@auth_blue_print.route("/signup")
def sign_up(request):
    
    return Response(data={"name": "Funso joba"})