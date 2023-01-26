from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login
import base64
import os

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    # Added two more columns for token and token_expiration
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()
        

    def __repr__(self):
        return f"<User: {self.id} | {self.username}>"

    def check_password(self, password_guess):
        return check_password_hash(self.password, password_guess)


    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'date_created': self.date_created,
            'posts': [p.to_dict() for p in self.posts.all()]
        }
    
    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(minuest=1):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.commit()
        return self.token

    def revoke_token(self):
        now = datetime.utcnow()
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)
        db.session.commit()

    # @staticmethod
    # def check_token(token):
    #     user = User.query.filter_by(token=token).first()
    #     if user is None or user.token_expiration < datetime.utcnow():
    #         return None
    #     return user

    
@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # SQL Equivalent - FOREIGHN KEY(user_id) REFERENCES user(id)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Post: {self.id} | {self.title}>"


        # Update method for the Post object
    def update(self, **kwargs):
        # for each key value that comes in as a keyword
        for key, value in kwargs.items():
            # if the key is an acceptable
            if key in {'title', 'body'}:
                # Set that attribute on the instance e.g post.title = 'Updated Title'
                setattr(self, key, value)
        # Save the updates to the database
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'date_created': self.date_created,
            'user_id': self.user_id,
            
        }

    
