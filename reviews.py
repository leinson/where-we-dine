from db import db
import datetime

def get_reviews(id):
    sql = "SELECT RV.review, RV.score, RV.visited, RV.sent_at, U.username FROM reviews RV, restaurants RE, users U WHERE RV.user_id=U.id AND RV.restaurant_id=RE.id AND RE.id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_restaurant_info(id):
    sql = "SELECT id, name, info, web_link, city FROM restaurants WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()

def get_restaurants():
    sql = "SELECT id, name FROM restaurants"
    result = db.session.execute(sql)
    return result.fetchall()

def submit_review(review, score, visited, restaurant_id, username):
    user_id = get_user_id(username)
    user_id = user_id[0]
    print(user_id, review, score, visited, restaurant_id)
    validated = validate_new_review(review, score, visited, user_id)
    if validated == True:
        sql = "INSERT INTO reviews (restaurant_id, user_id, review, score, visited, sent_at) VALUES (:restaurant_id, :user_id, :review, :score, :visited, LOCALTIMESTAMP(0))"
        db.session.execute(sql, {
            "restaurant_id":restaurant_id,
            "user_id":user_id,
            "review":review,
            "score":score,
            "visited":visited})
        db.session.commit()
        return True
    else:
        return validated

def add_restaurant(name, info, web_link, city, is_admin):
    if is_admin is False:
        return "You do not have rights to view this page"
    validate = validate_restaurant(name, info, city)
    if len(web_link) < 6:
        web_link = ""
    if validate == True:
        sql="INSERT INTO restaurants (name, info, web_link, city) VALUES (:name, :info, :web_link, :city)"
        db.session.execute(sql, {
                "name":name,
                "info":info,
                "web_link":web_link,
                "city":city})
        db.session.commit()
        return True
    else:
        return validate

def get_user_id(username):
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    return result.fetchone()

def validate_new_review(review, score, visited, user_id):
    message = True
    if user_id == 0:
        message = "No user id"
    if len(review) > 2000:
        message = "Your review is too long"
    if len(review) < 3:
        message = "Your review is too short"
    if int(score) not in [1,2,3,4,5,6,7,8,9,10]:
        message = "Incorrect score, should be a number between 1-10"
    if not validate_date(visited):
        message = "Incorrect date format, should be YYYY-MM-DD"
    return message

def validate_restaurant(name, info, city):
    print("validate restaurant")
    message = True
    if len(name) < 1 or len(name) > 100:
        message = "Incorrect input in field: name"
    if len(info) < 1 or len(info) > 2000:
        message = "Incorrect input in field: info"
    if len(city) < 1 or len(city) > 100:
        message = "Incorrect input in field: city"
    return message

def validate_date(visited):
    try:
        datetime.datetime.strptime(visited, "%Y-%m-%d")
    except ValueError:
        print("Date value error")
        return False 
    if int(visited[0:4]) < 1900:
        return False
    return True
