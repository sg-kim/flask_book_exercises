from flask import render_template, request, Blueprint

main = Blueprint('main', __name__)

@main.route("/ajax")
def home():
    return render_template("ajax.html")

@main.route("/ajax/request", methods=['POST'])
def respondAjax():
    data = request.json
    data['major'] = 'Physics'
    return data
