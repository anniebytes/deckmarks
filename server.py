from flask import Flask, request, session, flash, redirect
from flask.templating import render_template
import crud
import model

app = Flask(__name__)
model.connect_to_db(app)

@app.route('/')
def show_landing_page():
    return render_template("index.html")

@app.route('/groups')
def show_all_groups():
    groups = crud.get_all_groups()
    return render_template("groups.html", groups=groups)

@app.route('/login')
def show_login():
    return render_template("login.html")

@app.route('/process_login')
def process_login():
    """Gets data from login form and checks for email/password in db"""
    return render_template("login.html")

@app.route('/register')
def show_registration():
    return render_template("add_user_form.html")

@app.route('/create_user', methods=['POST'])
def create_user():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')
    crud.create_user_record(fname,lname,email,password)

    # add flash message

    return redirect('/')


@app.route('/add_group')
def add_group_form():
    return render_template('add_group_form.html')

@app.route('/create_group', methods=['POST'])
def create_group():
    name = request.form.get('name')
    description = request.form.get('description')
    private = request.form.get('private')
    crud.create_group_record(name, description, private)
    return redirect('/')

@app.route('/add_deckmark')
def add_deckmark_form():
    return render_template('add_deckmark_form.html')

@app.route('/create_deckmark', methods=['POST'])
def create_deckmark():
    link = request.form.get('link')
    description = request.form.get('description')
    thumbnail = request.form.get('thumbnail')
    crud.create_deckmark_record(link, description, thumbnail)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)