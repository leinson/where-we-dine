from db import db

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
    if user_id == 0:
        return False

    sql = "INSERT INTO reviews (restaurant_id, user_id, review, score, visited, sent_at) VALUES (:restaurant_id, :user_id, :review, :score, :visited, LOCALTIMESTAMP(0))"
    db.session.execute(sql, {
        "restaurant_id":restaurant_id,
        "user_id":user_id,
        "review":review,
        "score":score,
        "visited":visited})
    db.session.commit()
    return True


def get_user_id(username):
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    return result.fetchone()