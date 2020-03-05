from flask import Flask, render_template, url_for, redirect, request
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd2eb5380841f5fdc4b70bb3e8be4a614'

posts = [
        {
                'author': 'Elsa',
                'title': 'Blog Post 1',
                'content': 'The first post content',
                'date_posted': 'November 20, 2019'
        },
        {
                'author': 'Anna',
                'title': 'Blog Post 2',
                'content': 'The second post content',
                'date_posted': 'November 21, 2019'
        }
]

@app.route("/")
@app.route("/home")
def     home():
    return render_template("home.html", posts = posts)

@app.route("/about")
def	about():
    return render_template("about.html", title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print('Account created successfully')
        return redirect(url_for('home'))
    return render_template("register.html", title = 'Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@abc.com' and form.password.data == 'password':
            print('You have been logged in!')
            return redirect(url_for('home'))
        else:
            print('Login Unsuccessful. Please check username and password')
    return render_template("login.html", title = 'Login', form=form)

if __name__ == "__main__":
        app.run('127.0.0.1', 5000)
