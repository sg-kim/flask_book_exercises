from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class PostForm(FlaskForm):
        title = StringField('Title', validators=[DataRequired(), Length(min=1, max=90)])
        content = TextAreaField('Content', validators=[DataRequired(), Length(min=1, max=200)])
        submit = SubmitField('Post')
