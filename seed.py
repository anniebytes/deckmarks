"""Seed file to create tables and populate records in database"""
import model

def create_deckmark_records():
    link1 = {
        "user_id": 1,
        "link": "https://www.slideshare.net/e2m/flask-sqlalchemy",
        "description": "Python CodeLabs - Intro to Flask SQLAlchemy \n \
                        http://eueung.github.io/python/flask-sqlalchemy",
        "thumbnail": "www.somesite.com/someimg.jpg"
    }

    deckmark = model.Deckmark(
                        user_id = link1["user_id"],
                        link=link1["link"], 
                        description=link1["description"], 
                        thumbnail=link1["thumbnail"])

    model.db.session.add(deckmark)
    model.db.session.commit()

def create_group_records():
    group1 = {
        "user_id": 1,
        "name": "Hogwarts 2022",
        "description": "Hogwarts School of Magic Winter 2022",
        "private": False
    }

    group = model.Group(
                        user_id = group1["user_id"],
                        name=group1["name"], 
                        description=group1["description"], 
                        private=group1["private"])

    model.db.session.add(group)
    model.db.session.commit()


def create_category_records():
    category_names = ["Technology", "Business", "Art"]

    category_records = []

    for category in category_names: 
        category_records.append(model.Category(name=category))

    model.db.session.add_all(category_records)
    model.db.session.commit()

def create_user_records():
    hp = {
        "fname": "Harry",
        "lname": "Potter",
        "email": "harrypotter@hogwarts.edu",
        "password": "ilovegryffindor"
    }

    user1 = model.User(
                    fname=hp["fname"], 
                    lname=hp["lname"], 
                    email=hp["email"], 
                    password=hp["password"])

    model.db.session.add(user1)
    model.db.session.commit()

def create_tag_records():
    tag= model.Tag(name="tech")
    model.db.session.add(tag)
    model.db.session.commit()


if __name__ == "__main__":
    import model
    from server import app

    model.connect_to_db(app)

    # Drop and Create Tables
    model.db.drop_all()
    model.db.create_all()

    # Create Records
    create_user_records()
    create_category_records()
    create_group_records()
    create_deckmark_records()
    create_tag_records()