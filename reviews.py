from db import db

def get_reviews_and_info(id):
    sql = "SELECT RV.review, RE.name, RV.score, U.username FROM reviews RV, restaurants RE, users U WHERE RV.restaurant_id=RE.id AND RV.user_id=U.id AND RE.id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_restaurant_info(id):
    sql = "SELECT name, info, web_link, city FROM restaurants WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()

def get_restaurants():
    sql = "SELECT id, name FROM restaurants"
    result = db.session.execute(sql)
    return result.fetchall()

