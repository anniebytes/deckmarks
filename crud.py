"""CRUD functions for updating the database"""

import model

def create_deckmark(link, description, thumbnail):
    deckmark = model.Deckmark(link=link, description=description, thumbnail=thumbnail)
    model.db.session.add(deckmark)
    model.db.session.commit()

def create_group(name, description):
    group = model.Group(name=name, description=description)
    model.db.session.add(group)
    model.db.session.commit()

def get_group_id(name):
    """Returns group object"""
    return model.Group.query.filter(Group.name == name).one()

def get_all_groups():
    """Returns list of group objects"""
    return model.Group.query.all()

def add_deckmark_to_group(group_id, deckmark_id):
    """Creates deckmark in database with group and deckmark object"""
    new_item = model.groupItem(group_id=group_id, deckmark_id=deckmark_id)
    model.db.session.add(new_item)
    model.db.session.commit()

if __name__ == "__main__":
    from server import app
    model.connect_to_db(app)