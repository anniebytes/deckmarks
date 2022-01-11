""" ORM Model class definitions for deckmarks psql db"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import ForeignKey

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

    group = db.relationship("Group", secondary="group_items", backref="deckmarks")
    tags = db.relationship("Tag", secondary="decktags", backref="deckmarks")

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(1000), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Group(db.Model):

    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    private = db.Column(db.Boolean)

    # backref attributes:
    # .deckmarks - display deckmarks under a group

class groupItem(db.Model):
    """Association table between groups and deckmarks"""

    __tablename__ = "group_items"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    group_id = db.Column(db.Integer, ForeignKey('groups.id'))
    deckmark_id = db.Column(db.Integer, ForeignKey('deckmarks.id'))

class Tag(db.Model):

    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(1000), nullable=False)

    # backref attributes:
    # .deckmarks - display all deckmarks under a tag

class Decktag(db.Model):
    """Association table between deckmarks and tags"""

    __tablename__ = "decktags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    deckmark_id = db.Column(db.Integer, ForeignKey('deckmarks.id'))
    tag_id = db.Column(db.Integer, ForeignKey('tags.id'))

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///deckmarks"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db!")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)