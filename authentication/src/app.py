from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from dotenv import load_dotenv, dotenv_values

from decouple import config as env_config

from blueprints.signup_bp import signup_blue_print

# load_dotenv()

app = Flask(__name__)
app.register_blueprint(signup_blue_print, url_prefix="/auth/")


app.config['SQLALCHEMY_DATABASE_URI'] = env_config('SQLALCHEMY_DATABASE_URI')



if __name__ == "__main__":
    app.run(debug=True, port=5001)