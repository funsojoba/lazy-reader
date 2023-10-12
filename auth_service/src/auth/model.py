from src.db import db
import uuid




def get_username(data):
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    
    additional_symbols = "0123456789_"
    usernames = []
    for i in range(8):
        first_letter = first_name[0:i+1]
        last_letter = last_name[0:len(last_name)-i]
        first_and_last_name = f"@{first_letter}{last_letter}"
        username = first_and_last_name + "".join(random.choices(additional_symbols, k=8 - len(first_and_last_name)))
        usernames.append(username)
    return username[0]


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(254), default=uuid.uuid4())
    username = db.Column(db.String(80), unique=False, nullable=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, password, first_name, last_name, email, username=None):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name  

    @property
    def get_name(self):
        return self.first_name + " " + self.last_name

    def __repr__(self):
        return f"<User {self.first_name} {user.last_name}>"
