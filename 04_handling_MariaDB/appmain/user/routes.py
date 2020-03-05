from flask import Blueprint
from appmain import app, db
from appmain.user.models import Userdata

user = Blueprint('user', __name__)

@user.route('/init_db')
def initDB():
    print('initialize DB')
    db.create_all()
    return "<h2>Tables created.</h2>"

@user.route('/create_data')
def createData():
    userdata = Userdata(username = 'Anna', email = 'anna@abc.com')
    db.session.add(userdata)
    db.session.commit()
    return "<h2>User data created.</h2>"

@user.route('/read_data')
def readData():
    userdata = db.session.query(Userdata).filter_by(id = '1')
    print(userdata)
    return "<h2>Data read: " + userdata[0].username + ", " + userdata[0].email + "</h2>"
