import json
from database import db

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
  __tablename__ = "users"
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), nullable=False, unique=True)
  password_hash = db.Column(db.String(128), nullable=False)
  roles = db.Column(db.String(50), nullable=False)
  
  def __init__(self,username,password,roles=["user"]):
    self.username=username
    self.password_hash=generate_password_hash(password)
    self.roles=json.dumps(roles)
    
  def save(self):
    db.session.add(self)
    db.session.commit()
    
  @staticmethod
  def get_user_by_username(username):
    return User.query.filter_by(username=username).first()
  
