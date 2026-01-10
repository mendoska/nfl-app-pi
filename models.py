from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create database instance (we'll import this in app.py)
db = SQLAlchemy()

class User(db.Model):
    """
    User account table
    Each row = one user
    """

    __tablename__ = 'users'

    #Columns 
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password_hash = db.Column (db.Sring (255), nullable = False)
    created_at = db.Column (db.DateTime, default = datetime.utcnow)
    