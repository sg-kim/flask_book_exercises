from flask import render_template, url_for, redirect, request, Blueprint
from appmain.user.forms import RegistrationForm
from appmain.user.models import Userdata
from appmain import app, db, bcrypt
from flask_login import current_user

user = Blueprint('user', __name__)

@user.route("/register", methods=['GET', 'POST'])
def register():
        if current_user.is_authenticated:
                return redirect(url_for('main.home'))
        form = RegistrationForm()
        if form.validate_on_submit():
                hashedPassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                user = Userdata(username=form.username.data, email=form.email.data, password=hashedPassword)
                db.session.add(user)
                db.session.commit()
                print('An account has been created as ', form.username.data)
                return redirect(url_for('main.home'))
        return render_template("register.html", title='Register', form=form)
