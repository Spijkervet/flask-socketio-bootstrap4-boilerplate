'''
Boilerplate Python3 Flask SocketIO app

Janne Spijkervet, 2017
'''
from flask import Flask
from flask_socketio import SocketIO
from .info import Info
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt


__version__ = '1.0.0'

app_info = Info()
socketio = SocketIO()
db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app(host, debug):
    from . import events

    app = Flask(__name__)

    app.host = host
    app.debug = debug
    app.config['SECRET_KEY'] = 'Aqewur381!%*'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .views.index import index_bp
    from .views.login import login_bp
    app.register_blueprint(index_bp)
    app.register_blueprint(login_bp)

    socketio.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    return app
