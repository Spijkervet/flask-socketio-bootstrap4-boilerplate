from flask_wtf import FlaskForm
from wtforms.fields import StringField, BooleanField, SubmitField
from wtforms.validators import Required


class LoginForm(FlaskForm):
    username = StringField("Name", validators=[Required()], render_kw={"placeholder": "Username", "class": "form-control"})
    password = StringField("Password", validators=[Required()], render_kw={"placeholder": "Password", "class": "form-control"})
    remember = BooleanField("Remember", render_kw={"class": "form-check-input"})
    submit = SubmitField("Login", render_kw={"class": "btn btn-md btn-primary btn-block"})
