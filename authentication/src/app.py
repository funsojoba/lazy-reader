from flask import Flask

from decouple import config as env_config

from blueprints.signup_bp import signup_blue_print

# load_dotenv()

app = Flask(__name__)
app.register_blueprint(signup_blue_print, url_prefix="/auth/")



if __name__ == "__main__":
    app.run(
        debug=env_config("DEBUG"), 
        host='0.0.0.0',
        port=env_config("WEB_PORT"))