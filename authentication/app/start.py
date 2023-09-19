import logging

from flask import Flask, json
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api

from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import BadRequest
from werkzeug.wrappers import Response

import core.settings as config

# from app.orders.routes import init_cart_routes
# from app.products.routes import init_product_routes
# from app.users.routes import init_auth_routes


# from core.commands import create_dummy_users_command
from core.error_handlers import AppError
from core.resources.database import db



class App:
    def __init__(self, db=db):
        self.app = Flask(__name__)
        self.logger = logging.getLogger("gunicorn.error")
        self.db = db

    def load_config(self):
        # load flask config from settings
        for k in dir(config):
            v = getattr(config, k)
            if not k.startswith("_") and k.upper() == k and not callable(v):
                self.app.config[k] = v

    def build_app(self):
        self.load_config()
        # set logging based on unicorn level
        self.app.logger.handlers = self.logger.handlers
        if __name__ != "main":
            self.app.logger.setLevel(self.logger.level)
        else:
            self.app.logger.setLevel(logging.DEBUG)
        self.app.logger.info(
            "Logger Configured w/level {}".format(self.app.logger.level)
        )

        self.app.db = self.build_db()
        CORS(self.app)
        JWTManager(self.app)
        Migrate(self.app, self.app.db)
        self.set_routes()

        return self.app
    
    def build_db(self):
        self.db.init_app(self.app)
        return self.db

    def set_routes(self):
        api = Api(self.app)
        # init_auth_routes(api)
        #NOTE: add your app routes here
        # init_product_routes(api)
        # init_cart_routes(api)
        self.set_home_route()

    def set_home_route(self):
        @self.app.route("/")
        def home():
            return json.dumps({"status": True, "message": "Welcome to the API"})

    def get_app(self):
        return self.app

    
app = App().build_app()