from db import db

def get_restaurant_info(id):
    sql = "SELECT id, name, info, web_link, city FROM restaurants WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()

def get_restaurants():
    sql = "SELECT id, name FROM restaurants"
    result = db.session.execute(sql)
    return result.fetchall()

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