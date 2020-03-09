from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd2eb5380841f5fdc4b70bb3e8be4a614'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskweb:your_password@localhost:3306/flaskdb'

db = SQLAlchemy(app)

from appmain.DBSession.routes import sess

app.register_blueprint(sess)

from appmain.DBSession.utils import SQLAlchemySessionInterface

app.session_interface = SQLAlchemySessionInterface()
