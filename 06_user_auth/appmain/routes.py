from flask import render_template, Blueprint

posts = [
        {
                'author': 'Elsa',
                'title': 'The first post',
                'content': 'First post content',
                'date_posted': 'Nov. 20, 2019'
        },
        {
                'author': 'Anna',
                'title': 'The second post',
                'content': 'Second post content',
                'date_posted': 'Nov. 21, 2019'
        }
]

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
        return render_template("home.html", posts=posts)

@main.route("/about")
def about():
        return render_template("about.html", title='About')
