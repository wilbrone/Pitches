from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_load
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    '''
    Class user that defines the user object that is sent to the database and password authentication on login
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    full_name = db.Column(db.String(255))
    bio = db.Column(db.String(300))
    pass_secure = db.Column(db.String(255))

    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")
    pitches = db.relationship('Pitch', backref = 'user', lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(arg):
        return f'User {self.username}'


class Pitch(object):
    """docstring for Pitch class that defines the piches object."""
    __tablename__ = 'pitches'

    id = db.Columns(db.Integer, primary_key = True)

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
