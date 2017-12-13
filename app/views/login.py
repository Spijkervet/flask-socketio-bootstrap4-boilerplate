from flask import render_template, redirect, request, url_for, Blueprint
from .. import app_info, login_manager
from ..forms import LoginForm
from ..models import User
from flask_login import login_user, logout_user, login_required, current_user


login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User(form.username.data, form.password.data)
            login_user(user) # login_user(user, remember=True)
            return redirect(url_for('index.index'))
    elif request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for('index.index'))

    return render_template('login.html', app_info=app_info, form=form)


@login_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    current_user.logout()
    logout_user()
    return redirect(url_for('login.login'))

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for("login.login"))


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)
