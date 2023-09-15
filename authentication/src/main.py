from flask import Flask
from blueprints.auth_bp import auth_blue_print


app = Flask(__name__)
app.register_blueprint(auth_blue_print, url_prefix="auth/")




if __name__ == "__main__":
    app.run(debug=True, port=5001)