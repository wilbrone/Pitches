from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
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
    email = db.Column(db.String(255))
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

    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(user_id))


    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    """docstring for Pitch class that defines the piches object. Getting pitches and single pitch"""
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    content = db.Column(db.String(1000))
    category = db.Column(db.String)
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)

    comments = db.relationship('Comment', backref = 'pitch', lazy = "dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,category):
        pitches = Pitch.query.filter_by(category = category).all()

        return pitches

    @classmethod
    def get_single_pitch(cls,id):
        single_pitch = Pitch.query.filter_by(id = id).first()

        return single_pitch

    @classmethod
    def count_pitches(cls,uname):
        user = User.query.filter_by(username = uname).first()
        pitches = Pitch.query.filter_by(user_id = user.id).all()

        pitches_count = 0
        for pitch in pitches:
            pitches_count += 1

        return pitches_count

class Comment(db.Model):
    """docstring for Comment. this defines the comment object and getting the comments based on the pitch id"""

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id = pitch_id).all()
