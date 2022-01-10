""" ORM Model class definitions for deckmarks psql db"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model): 
    
    __tablename__ = "categories"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(1000), nullable=False)

class Deckmark(db.Model): 

    __tablename__ = "deckmarks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    link = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.Text, nullable=True)
    thumbnail = db.Column(db.String(1000), nullable=True)

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(1000), nullable=False)
    password = db.Column(db.String(100), nullable=False)

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///deckmarks"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db!")


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)