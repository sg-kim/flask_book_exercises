from appmain import db, loginManager
from flask_login import UserMixin

@loginManager.user_loader
def load_user(userId):
        return Userdata.query.get(int(userId))

class Userdata(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(30), unique=True, nullable=False)
        email = db.Column(db.String(60), unique=True, nullable=False)
        picture = db.Column(db.String(20), nullable=False, default="default.png")
        password = db.Column(db.String(60), nullable=False)
