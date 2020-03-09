from flask import Blueprint, session

sess = Blueprint('session', __name__)

@sess.route("/set_session")
def setSession():
    session['userName'] = 'Christophe'
    return 'creating a session'

@sess.route("/get_session")
def getSession():
    if 'userName' in session:
        return session['userName']

    return 'session does not exist'

@sess.route("/delete_session")
def deleteSession():
    session.pop('userName', None)
    return 'deleting the session'
