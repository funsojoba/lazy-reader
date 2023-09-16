from .app import app

from uuid import uuid4
from decouple import config as env_config
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = env_config('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)


def get_uid():
    return uuid4().hex

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String, default=get_uid)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(554), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.first_name + " " + self.last_name