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

# Team page
@app.route("/team")
def team_page():
    return render_template("team_page.html")

# Menu page
@app.route("/menu2")
def menu_page():
    return render_template("menu_page2.html")

# Checkout page
@app.route("/checkout")
def checkout_page():
    return render_template("checkout.html")

