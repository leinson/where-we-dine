from flask import redirect, render_template, request, session, abort
from app import app
import users, reviews, restaurants


@app.route("/")
def index():
    user_id = users.is_logged_in()
    is_admin = users.is_admin()
    list = restaurants.get_restaurants()
    cuisines = restaurants.get_cuisines()
    return render_template("index.html", count=len(list), restaurants=list, cuisines=cuisines, is_admin=is_admin, user_id=user_id)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
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
    allow = False
    is_admin = users.is_admin()
    if is_admin:
        allow = True
    elif users.is_logged_in() == id:
        allow = True
    if not allow:
        return render_template("error.html", message="You do not have rights to view this page")
    list = users.get_users_reviews(id)
    return render_template("user.html", is_admin=is_admin, user_id=id, count=len(list), reviews=list)

@app.route("/reviews/<int:id>")
def show_reviews(id):
    is_admin = users.is_admin()
    user_id = users.is_logged_in()
    list = reviews.get_reviews(id)
    about = restaurants.get_restaurant_info(id)
    cuisines = restaurants.get_restaurants_cuisines(id)
    return render_template("reviews.html", is_admin=is_admin, user_id=user_id, count=len(list), reviews=list, restaurant=about, cuisines=cuisines)

@app.route("/new-review/<int:id>", methods=["GET", "POST"])
def new_review(id):
    if request.method == "GET":
        user_id = users.is_logged_in()
        restaurant_info = restaurants.get_restaurant_info(id)
        return render_template("new-review.html", user_id=user_id, restaurant=restaurant_info)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        review = request.form.get("review", "")
        score = request.form.get("score", "").strip()
        visited = request.form.get("visited", "").strip()
        restaurant_id = id
        username = users.username()
        submit = reviews.submit_review(review, score, visited, restaurant_id, username)
        if submit == True:
            return redirect("/reviews/" + str(restaurant_id))
        return render_template("error.html", message=submit)

@app.route("/new-restaurant", methods=["GET", "POST"])
def new_restaurant():
    if request.method == "GET":
        is_admin = users.is_admin()
        user_id = users.is_logged_in()
        list = restaurants.get_cuisines()
        if is_admin:
            return render_template("new-restaurant.html", is_admin=is_admin, user_id=user_id, cuisines=list)
        return render_template("error.html", message="You do not have rights to view this page")
    if request.method == "POST":
        is_admin = users.is_admin()
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        if is_admin:
            name = request.form.get("name", "")
            info = request.form.get("info", "")
            web_link = request.form.get("web_link", "").strip()
            city = request.form.get("city", "")
            price = request.form.get("price", "")
            cuisines = request.form.getlist("cuisine")
            submit = restaurants.add_restaurant(name, info, web_link, city, price, is_admin, cuisines)
            if submit == True:
                return redirect("/")
            return render_template("error.html", message=submit)
        return render_template("error.html", message="You do not have rights to view this page")

@app.route("/delete_review/<int:id>", methods=["POST"])
def delete_review(id):
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        reviews.delete_review(id)
        user_id = users.is_logged_in()
        return redirect("/user/"+ str(user_id))
    return render_template("error.html", message="Could not delete review")

@app.route("/delete_user/<int:id>", methods=["POST"])
def delete_user(id):
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        users.delete_user(id)
        return redirect("/")
    return render_template("error.html", message="Could not delete account")

@app.route("/cuisines", methods=["GET"])
def cuisines():
    is_admin = users.is_admin()
    user_id = users.is_logged_in()
    list = restaurants.get_cuisines()
    if is_admin:
        return render_template("cuisines.html", is_admin=is_admin, user_id=user_id, cuisines=list)
    return render_template("error.html", message="You do not have rights to view this page")
    
@app.route("/cuisines/add", methods=["POST"])
def add_cuisines():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    cuisine = request.form.get("cuisine", "")
    submit = restaurants.add_new_cuisine(cuisine)
    if submit == True:
        return redirect("/cuisines")
    return render_template("error.html", message="Could not add cuisine")

@app.route("/cuisines/delete/<int:id>", methods=["POST"])
def delete_cuisine(id):
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    if restaurants.delete_cuisine(id):
        return redirect("/cuisines")
    return render_template("error.html", message="Could not delete cuisine")

@app.route("/sort_by_cuisine", methods=["POST"])
def sort_by_cuisine():
    cuisine_id = request.form.get("cuisine_id", "")
    user_id = users.is_logged_in()
    is_admin = users.is_admin()
    list = restaurants.sort_by_cuisine(cuisine_id)
    cuisines = restaurants.get_cuisines()
    cuisine_name = restaurants.get_cuisine(cuisine_id)
    return render_template("index.html", count=len(list), restaurants=list, cuisines=cuisines, cuisine_name=cuisine_name, is_admin=is_admin, user_id=user_id)

@app.route("/sort_by_score", methods=["POST"])
def sort_by_score():
    score = request.form.get("score", "")
    user_id = users.is_logged_in()
    is_admin = users.is_admin()
    list = restaurants.sort_by_score(score)
    if list == False:
        return redirect("/")
    cuisines = restaurants.get_cuisines()
    return render_template("index.html", count=len(list), restaurants=list, cuisines=cuisines, is_admin=is_admin, user_id=user_id)
   

@app.route("/sort_by_price", methods=["POST"])
def sort_by_price():
    price = request.form.get("price", "")
    user_id = users.is_logged_in()
    is_admin = users.is_admin()
    list = restaurants.sort_by_price(price)
    if list == False:
        return redirect("/")
    cuisines = restaurants.get_cuisines()
    return render_template("index.html", count=len(list), restaurants=list, cuisines=cuisines, is_admin=is_admin, user_id=user_id)
