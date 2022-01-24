from flask import Flask, request, session, flash, redirect, jsonify
from flask.templating import render_template
import crud
import model
import ss_api
import parse_xml

app = Flask(__name__)
app.secret_key = 'DEV'
model.connect_to_db(app)

@app.route('/')
def view_landing_page():
    return render_template("index.html")

@app.route('/flash_test')
def flash_test():
    flash('hello')
    return render_template("flash.html")

# <----- Routes related to User ----->
@app.route('/login')
def show_login():
    return render_template("login.html")

@app.route('/check_user_login', methods=['POST'])
def check_user_login():
    """Gets data from login form and checks for email/password in db"""
    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.check_user_login(email,password)
    if user.id:
        session['user_id'] = user.id
        flash(f'Welcome back {user.fname}')
        return redirect('/')
    else:
        flash('Login unsuccessful', 'error')
    return redirect('/login')

@app.route('/register')
def view_registration():
    return render_template("add_user_form.html")

@app.route('/create_user', methods=['POST'])
def create_user():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')
    if crud.create_user_record(fname,lname,email,password):
        flash('new record created', 'message')
    else:
        flash('record creation failed', 'error')
    return redirect('/')

# <----- Routes related to Groups ----->
@app.route('/groups')
def view_all_groups():
    groups = crud.get_all_groups()
    return render_template("groups.html", groups=groups)


@app.route('/group/<id>')
def view_group(id):
    group = crud.get_deckmarks_by_group_id(id)
    return render_template("group_details.html", group=group)

@app.route('/add_group')
def add_group_form():
    if session.get('user_id'): 
        return render_template('add_group_form.html')
    return redirect('/')

@app.route('/create_group', methods=['POST'])
def create_group():
    user_id = session['user_id']
    if not user_id:
        flash('Must be a logged in user to create a group.')
        return redirect('/add_group')
    name = request.form.get('name')
    description = request.form.get('description')
    private = request.form.get('private')
    if crud.create_group_record(
                                user_id=user_id,
                                name=name,
                                description=description,
                                private=private):
            flash('new record created', 'message')
    else:
        flash('record creation failed', 'error')
    return redirect('/')

# <----- Routes related to Deckmarks ----->
@app.route('/deckmarks')
def view_all_deckmarks():
    deckmarks = crud.get_all_deckmarks()
    return render_template("deckmarks.html", deckmarks=deckmarks)

@app.route('/add_deckmark')
def add_deckmark_form():
    if session.get('user_id'): 
        return render_template('add_deckmark_form.html')
    flash('User must be logged in to access this page')
    return redirect('/')

@app.route('/create_deckmark', methods=['POST'])
def create_deckmark():
    user_id = session['user_id']
    if not user_id:
        flash('Must be a logged in user to create a group.')
        return redirect('/add_deckmark')
    if request.form.get('link'):
        link = request.form.get('link')
        description = request.form.get('description')
        thumbnail = request.form.get('thumbnail')
    if request.json.get('link'):
        link = request.json.get('link')
        description = request.json.get('description')
        thumbnail = request.json.get('thumbnail')
    deckmark = crud.create_deckmark_record(
                                user_id=user_id,
                                link=link,
                                description=description,
                                thumbnail=thumbnail)
    if deckmark:
        flash('new record created', 'message')
    else:
        flash('record creation failed', 'error')
    
    # Create new group item
    group_id = request.form.get('group_id')
    if group_id and crud.add_deckmark_to_group(group_id, deckmark.id):
        flash(f"new deckmark added to group_id: {group_id}")
        return redirect(f"/group/{group_id}")
    else:
        flash('record creation failed', 'error')
    return redirect("/groups")

@app.route('/deckmark/<id>/tags')
def view_deckmark_tags(id):
    json_dict = crud.get_tags_by_deckmark_id(id)
    return jsonify(json_dict)

@app.route('/browse/slideshare/<tag>')
def slideshare_api(tag):
    response_text = ss_api.api_request(tag)
    print(response_text)
    if response_text == False:
        print("No valid response from Slideshare API. Redirecting to /.")
        return redirect('/')
    else:
        slideshow_list = parse_xml.slideshow_list(response_text)
        groups = crud.get_all_groups()
        return render_template('response.html', slideshow_list=slideshow_list, groups=groups)

@app.route('/api/add_tag_to_deckmark', methods=["POST"])
def add_tag_to_deckmark():
    deckmark_id = request.json.get('deckmark_id')
    tag_id = request.json.get('tag_id')
    if crud.add_tag_to_deckmark(deckmark_id, tag_id):
        return {"success": True}
    else:
        return {"success": False}

@app.route('/api/create_tag', methods=["POST"])
def create_tag():
    tag_name = request.json.get('name')
    tag_id = crud.create_tag(tag_name)
    if tag_id:
        return {"tag_id": tag_id}
    else:
        return {"success": False}

if __name__ == "__main__":
    app.run(debug=True)