from flask import Flask
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

if __name__ == "__main__":
    app.run(debug=True)