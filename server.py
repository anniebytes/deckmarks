from flask import Flask, request, session, flash, redirect
from flask.templating import render_template
import crud
import model

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
    if username is not False:
        session['user_logged_in'] = True
        flash(f'Welcome back {username}')
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
    return render_template("group_details.html", deckmarks=group.deckmarks)


@app.route('/add_group')
def add_group_form():
    if session.get('user_logged_in'): 
        return render_template('add_group_form.html')
    return redirect('/')

@app.route('/create_group', methods=['POST'])
def create_group():
    name = request.form.get('name')
    description = request.form.get('description')
    private = request.form.get('private')
    if crud.create_group_record(name, description, private):
            flash('new record created', 'message')
    else:
        flash('record creation failed', 'error')
    return redirect('/')

# <----- Routes related to Deckmarks ----->
@app.route('/add_deckmark')
def add_deckmark_form():
    if session.get('user_logged_in'): 
        return render_template('add_deckmark_form.html')
    flash('User must be logged in to access this page')
    return redirect('/')

@app.route('/create_deckmark', methods=['POST'])
def create_deckmark():
    link = request.form.get('link')
    description = request.form.get('description')
    thumbnail = request.form.get('thumbnail')
    if crud.create_deckmark_record(link, description, thumbnail):
            flash('new record created', 'message')
    else:
        flash('record creation failed', 'error')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)