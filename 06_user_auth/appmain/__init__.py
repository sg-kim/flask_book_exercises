from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd2eb5380841f5fdc4b70bb3e8be4a614'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskweb:your_password@localhost:3306/flaskdb'

db = SQLAlchemy(app)

loginManager = LoginManager(app)

bcrypt = Bcrypt(app)

from appmain.user.routes import user
from appmain.routes import main

db.create_all()

loginManager.login_view = 'user.login'

app.register_blueprint(user)
app.register_blueprint(main)
