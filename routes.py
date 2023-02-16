from flask import redirect, render_template, request
from app import app
import users, reviews, restaurants


@app.route("/")
def index():
    user_id = users.is_logged_in()
    is_admin = users.is_admin()
    list = restaurants.get_restaurants()
    return render_template("index.html", count=len(list), restaurants=list, is_admin=is_admin, user_id=user_id)

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
            return render_template("error.html", message="Registeration unsuccessful, invalid username or password")

@app.route("/user/<int:id>")
def user(id):
    print("user page id: ", id)
    allow = False
    is_admin = users.is_admin()
    if is_admin:
        allow = True
    elif users.is_logged_in() == id:
        allow = True
    if not allow:
        return render_template("error.html", message="You do not have rights to view this page")
    list = users.get_users_reviews(id)
    print(list)
    return render_template("user.html", is_admin=is_admin, count=len(list), reviews=list)

@app.route("/reviews/<int:id>")
def show_reviews(id):
    list = reviews.get_reviews(id)
    about = restaurants.get_restaurant_info(id)
    cuisines = restaurants.get_restaurants_cuisines(id)
    return render_template("reviews.html", count=len(list), reviews=list, restaurant=about, cuisines=cuisines)

@app.route("/new-review/<int:id>", methods = ["GET", "POST"])
def new_review(id):
    if request.method == "GET":
        restaurant_info = restaurants.get_restaurant_info(id)
        return render_template("new-review.html", restaurant = restaurant_info)
    
    if request.method == "POST":
        review = request.form.get("review", "")
        score = request.form.get("score", "").strip()
        visited = request.form.get("visited", "").strip()
        restaurant_id = id
        username = users.username()
        submit = reviews.submit_review(review, score, visited, restaurant_id, username)
        if submit == True:
            return redirect("/reviews/" + str(restaurant_id))
        else:
            return render_template("error.html", message=submit)

@app.route("/new-restaurant", methods = ["GET", "POST"])
def new_restaurant():
    if request.method == "GET":
        is_admin = users.is_admin()
        print("new restaurant GET method")
        list = restaurants.get_cuisines()
        if is_admin:
            return render_template("new-restaurant.html", is_admin=is_admin, cuisines=list)
        else:
            return render_template("error.html", message="You do not have rights to view this page")
    if request.method == "POST":
        is_admin = users.is_admin()
        if is_admin:
            name = request.form.get("name", "")
            info = request.form.get("info", "")
            web_link = request.form.get("web_link", "").strip()
            city = request.form.get("city", "")
            price = request.form.get("price", "")
            cuisines = request.form.getlist("cuisine")
            print("new restaurant - POST values:", name, info, web_link, city, price, is_admin, cuisines)
            submit = restaurants.add_restaurant(name, info, web_link, city, price, is_admin, cuisines)
            if submit == True:
                return redirect("/")
            else:
                return render_template("error.html", message=submit)
        else:
            return render_template("error.html", message="You do not have rights to view this page")