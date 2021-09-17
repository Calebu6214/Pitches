
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
# from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    '''
    Callback function that retrieves a user when a unique identifier is passed
    '''
    return User.query.get(int(user_id))


class User( db.Model):
    '''
    Class that creates new users
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    other_names = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    profile_pic_path = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        '''
        Method to block access to the password property
        '''
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        '''
        Method to generate a password hash
        Args:
            password: password to hash
        '''
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        '''
        Method to verify the password on login
        Args:
            password: password to verify
        '''
        return check_password_hash(self.password_hash, password)

    def save_user(self):
        '''
        Method that saves the instance of user model
        '''
        db.session.add(self)
        db.session.commit()