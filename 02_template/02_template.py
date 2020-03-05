from flask import Flask, render_template, url_for
app = Flask(__name__)

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
def	home():
    return render_template("home.html", posts = posts)

@app.route("/about")
def	about():
    return render_template("about.html", title = 'About')

if __name__ == "__main__":
    app.run("127.0.0.1", 5000)
