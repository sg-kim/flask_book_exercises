from flask import Blueprint, session

sess = Blueprint('session', __name__)

@sess.route("/create_dbsession")
def createDBSession():
    session['userEmail'] = 'bart@abc.com'

    return 'a session has been created.'

@sess.route("/get_dbsession")
def getDBSession():
    useremail = session.get('userEmail')

    return 'user email: ' + useremail

@sess.route("/delete_dbsession")
def deleteDBSession():
    session.clear()

    return 'the session has been removed'
