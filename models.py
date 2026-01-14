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
    password_hash = db.Column (db.String (255), nullable = False)
    created_at = db.Column (db.DateTime, default = datetime.utcnow)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Favorite (db.Model):
    """
    Favorite teams table
    Each row = one team that one user likes
    """
    __tablename__ = 'favorites'

    #Columns
    id = db.Column (db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    team_name = db.Column(db.String(100), nullable = False)
    sport = db.Column (db.String(10), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f'<Favorite {self.team_name}>'
