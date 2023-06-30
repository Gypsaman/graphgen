from flask_login import UserMixin
from webproject.modules.extensions import db
from datetime import datetime

class Users(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    role = db.Column(db.String(10))
    
    def __repr__(self):
        return f"User('{self.email}', '{self.first_name}', '{self.last_name}', '{self.role}')"