from db import db

def get_restaurant_info(id):
    sql = "SELECT id, name, info, web_link, city, price FROM restaurants WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()

def get_restaurants_cuisines(id):
    restaurant_id = id
    sql = "SELECT C.cuisine FROM cuisines C, restaurant_cuisines RC WHERE RC.cuisine_id=C.id AND RC.restaurant_id=:restaurant_id"
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    return result.fetchall()

def get_restaurants():
    sql = "SELECT RE.id, RE.name, COALESCE(round(AVG(RV.score)::numeric,2),'0') FROM restaurants RE LEFT JOIN reviews RV ON RV.restaurant_id=RE.id GROUP BY RE.name, RE.id"
    result = db.session.execute(sql)
    return result.fetchall()

def add_restaurant(name, info, web_link, city, price, is_admin, cuisines):
    if is_admin is False:
        return "You do not have rights to view this page"
    validate = validate_restaurant(name, info, city, price)
    if len(web_link) < 6:
        web_link = ""
    if validate == True:
        sql="INSERT INTO restaurants (name, info, web_link, city, price) VALUES (:name, :info, :web_link, :city, :price)"
        db.session.execute(sql, {
                "name":name,
                "info":info,
                "web_link":web_link,
                "city":city,
                "price":price})
        add_restaurant_cuisines(name, cuisines)
        db.session.commit()
        return True
    else:
        return validate

def validate_restaurant(name, info, city, price):
    print("validate restaurant")
    message = True
    if len(name) < 1 or len(name) > 100:
        message = "Incorrect input in field: name"
    if len(info) < 1 or len(info) > 2000:
        message = "Incorrect input in field: info"
    if len(city) < 1 or len(city) > 100:
        message = "Incorrect input in field: city"
    prices = ["€", "€€", "€€€"]
    if price not in prices:
        message = "Incorrect input in field: price"
    return message

def add_restaurant_cuisines(name, cuisines):
    sql="SELECT id FROM restaurants WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    restaurant_id=result.fetchone()
    restaurant_id = restaurant_id[0]
    cuisine_ids=[]
    for cuisine in cuisines:
        sql = "SELECT id FROM cuisines WHERE cuisine=:cuisine"
        result = db.session.execute(sql, {"cuisine":cuisine})
        result = result.fetchone()
        result = result[0]
        cuisine_ids.append(result)
    for cuisine_id in cuisine_ids:
        sql="INSERT INTO restaurant_cuisines (restaurant_id, cuisine_id) VALUES (:restaurant_id, :cuisine_id)"
        db.session.execute(sql, {
                "restaurant_id":restaurant_id,
                "cuisine_id":cuisine_id})
    return True

def get_cuisines():
    sql = "SELECT id, cuisine FROM cuisines"
    result = db.session.execute(sql)
    return result.fetchall()

def add_new_cuisine(cuisine):
    if len(cuisine) > 2 and len(cuisine) < 25:
        sql = "INSERT INTO cuisines (cuisine) VALUES (:cuisine)"
        db.session.execute(sql, {"cuisine":cuisine})
        db.session.commit()
        return True
    return False

def delete_cuisine(id):
    sql = "DELETE FROM cuisines WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True

def get_one_average_score(id):
    #For the restaurants own reviews page
    sql = "SELECT COALESCE(round(AVG(score)::numeric,2),'0') FROM reviews WHERE restaurant_id=:id"
    result = db.session.execute(sql, {"restaurant_id":id})
    result = result.fetchone()
    result = "{:.2f}".format(result[0])
    return result

def sort_by_cuisine(id):
    sql = "SELECT RE.id, RE.name, COALESCE(round(AVG(RV.score)::numeric,2),'0') FROM restaurants RE, reviews RV, restaurant_cuisines RC WHERE RV.restaurant_id=RE.id AND RC.restaurant_id=RV.restaurant_id AND RC.cuisine_id=:id GROUP BY RE.name, RE.id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_cuisine(id):
    sql = "SELECT cuisine FROM cuisines WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    result = result.fetchone()
    return result[0]