from flask import make_response, Blueprint, request

cookie = Blueprint('main', __name__)

@cookie.route("/set_cookie")
def setCookie():
    resp = make_response("setting up a cookie")
    resp.set_cookie("userId", "12345")

    return resp

@cookie.route("/get_cookie")
def getCookie():
    userId = request.cookies.get("userId")
    return 'user ID is ' + userId

@cookie.route("/delete_cookie")
def deleteCookie():
    resp = make_response("deleting the cookie")
    resp.set_cookie("userId", "", expires=0)

    return resp
