# To test the sight
# set FLASK_DEBUG=1
# set FLASK_APP=group13_website.py
# flask run

from flask import Flask, render_template
app = Flask(__name__)

# Home Page
@app.route("/")
@app.route('/home')
def home_page():
    return render_template("home_page.html")

@app.route("/team")
def team_page():
    return render_template("team_page.html")
