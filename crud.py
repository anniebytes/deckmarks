"""CRUD functions for updating the database"""

import model

def create_user_record(fname, lname, email, password):
    user = model.User(fname=fname, lname=lname, email=email, password=password)
    model.db.session.add(user)
    model.db.session.commit()
    return True

def check_user_login(email, password):
    user = model.User.query.filter(model.User.email == email).one()
    if user and user.password == password:
        return user
    return False

def create_deckmark_record(user_id, link, description, thumbnail):
    deckmark = model.Deckmark(user_id=user_id, link=link, description=description, thumbnail=thumbnail)
    model.db.session.add(deckmark)
    model.db.session.commit()
    return True

def create_group_record(user_id, name, description,private=False):
    group = model.Group(user_id=user_id, name=name, description=description,private=private)
    model.db.session.add(group)
    model.db.session.commit()
    return True

def get_group_id(name):
    """Returns group object"""
    return model.Group.query.filter(Group.name == name).one()

def get_all_groups():
    """Returns list of group objects"""
    return model.Group.query.all()

def get_deckmarks_by_group_id(group_id):
    """Returns group object"""
    # add validation that only one group is returned
    return model.Group.query.filter(model.Group.id == group_id).one()

def add_deckmark_to_group(group_id, deckmark_id):
    """Creates association between group and deckmark"""
    group_item = model.groupItem(group_id=group_id, deckmark_id=deckmark_id)
    model.db.session.add(group_item)
    model.db.session.commit()
    return group_item

def add_tag_to_deckmark(deckmark_id, tag_id):
    """Creates association between deckmark and tag"""
    tag = model.Decktag(deckmark_id=deckmark_id, tag_id=tag_id)
    model.db.session.add(tag)
    model.db.session.commit()

if __name__ == "__main__":
    from server import app
    model.connect_to_db(app)