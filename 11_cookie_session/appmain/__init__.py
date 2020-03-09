from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd2eb5380841f5fdc4b70bb3e8be4a614'

from appmain.cookie.routes import cookie
from appmain.session.routes import sess

app.register_blueprint(cookie)
app.register_blueprint(sess)
