from flask_login import UserMixin
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from app import db, bcrypt

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class User(UserMixin, Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, username=None, password=None):
        if username and password:
            self.username = username
            self.password = bcrypt.generate_password_hash(password)


    def check_password(self, password):
        bcrypt.check_password_hash(pw_hash, password)

    def logout(self):
        print("Logged out")

# Create tables.
Base.metadata.create_all(bind=engine)
