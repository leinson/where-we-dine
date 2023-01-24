from db import db

def get_reviews():
    sql = "SELECT RV.review, RE.name, RV.score, U.username FROM reviews RV, restaurants RE, users U WHERE RV.restaurant_id=RE.id AND RV.user_id=U.id"
    result = db.session.execute(sql)
    return result.fetchall()
    