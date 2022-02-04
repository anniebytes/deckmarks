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
    return None

def create_deckmark_record(user_id, link, description, thumbnail):
    deckmark = model.Deckmark(user_id=user_id, link=link, description=description, thumbnail=thumbnail)
    model.db.session.add(deckmark)
    model.db.session.commit()
    return deckmark

def create_group_record(user_id, name, description,private=False):
    group = model.Group(user_id=user_id, name=name, description=description,private=private)
    model.db.session.add(group)
    model.db.session.commit()
    return True

def update_group_name(id, name, new_name):
    """Returns group object"""
    print("NEW:" + new_name)
    if id == 'none':
        group = model.Group.query.filter(model.Group.name == name).first()
    elif name == 'none':
        group = model.Group.query.filter(model.Group.id == id).one()
    group.name = new_name
    print("group.name:" + group.name)
    model.db.session.add(group)
    model.db.session.commit()
    return group

def get_group_item_id(group_id, deckmark_id):
    group_item = model.groupItem.query.filter((model.groupItem.group_id == group_id) & (model.groupItem.deckmark_id == deckmark_id)).one()
    if group_item:
        return group_item.id 
    return None

def delete_group_item(group_item_id):
    group_item = model.groupItem.query.filter(model.groupItem.id == group_item_id).one()
    model.db.session.delete(group_item)
    model.db.session.commit()
    return {"status": f"group_item_id {group_item_id} has been deleted from the db."}

def get_group_id(name):
    """Returns group object"""
    return model.Group.query.filter(model.Group.name == name).one()

def get_all_groups():
    """Returns list of group objects"""
    return model.Group.query.all()

def get_all_deckmarks():
    """Returns list of deckmark objects"""
    return model.Deckmark.query.all()

def get_deckmarks_by_group_id(group_id):
    """Returns group object"""
    # add validation that only one group is returned
    return model.Group.query.filter(model.Group.id == group_id).one()

def get_deckmarks_by_user(user_id):
    return model.Deckmark.query.filter(model.Deckmark.user_id == user_id).all()

def add_deckmark_to_group(group_id, deckmark_id):
    """Creates association between group and deckmark"""
    group_item = model.groupItem(group_id=group_id, deckmark_id=deckmark_id)
    model.db.session.add(group_item)
    model.db.session.commit()
    return group_item

def get_tags_by_deckmark_id(deckmark_id):
    """Returns JSON string of tags"""
    tags_list = model.Deckmark.query.filter(model.Deckmark.id == deckmark_id).one().tags
    json_dict = { "tags" : "" }
    for tag in tags_list:
        json_dict["tags"] += tag.name
    return json_dict

def create_tag(name):
    tag = model.Tag(name=name)
    model.db.session.add(tag)
    model.db.session.commit()
    return tag.id

def add_tag_to_deckmark(deckmark_id, tag_id):
    """Creates association between deckmark and tag"""
    tag = model.Decktag(deckmark_id=deckmark_id, tag_id=tag_id)
    model.db.session.add(tag)
    model.db.session.commit()
    if tag:
        return True
    return None

if __name__ == "__main__":
    from server import app
    model.connect_to_db(app)