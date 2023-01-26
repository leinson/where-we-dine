from flask import redirect, render_template, request
from app import app
import users, reviews


@app.route("/")
def index():
    list = reviews.get_restaurants()
    return render_template("index.html", count=len(list), restaurants=list)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Wrong username or password")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="The passwords are not the same")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Registeration unsuccessful")

@app.route("/reviews/<int:id>")
def show_reviews(id):
    list = reviews.get_reviews(id)
    about = reviews.get_restaurant_info(id)
    return render_template("reviews.html", count=len(list), reviews=list, restaurant=about)

@app.route("/new-review/<int:id>")
def new_review(id, methods=["GET", "POST"]):
    #in progress next
    return render_template("new-review.html")
