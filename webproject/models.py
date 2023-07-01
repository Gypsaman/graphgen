from flask_login import UserMixin
from webproject.modules.extensions import db
from datetime import datetime

class Users(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    role = db.Column(db.String(10))
    
    def __repr__(self):
        return f"User('{self.email}', '{self.first_name}', '{self.last_name}', '{self.role}')"
    
class PasswordReset(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    password_phrase = db.Column(db.Integer)
    phrase_expires = db.Column(db.DateTime)
    
    def get_password_phrase(self):
        return self.password_phrase
    
    def get_password_phrase_expiry(self) -> datetime:
        return self.phrase_expires
    
    def __repr__(self):
        return f'password_phrase: {self.password_phrase}, phrase_expires: {self.phrase_expires}'
