from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT id, username, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["username"] = user.username
            return True
        else:
            return False

def logout():
    del session["username"]

def register(username, password):
    if check_registeration(username, password):
        hash_value = generate_password_hash(password)
        isadmin = "false"
        try:
            sql = "INSERT INTO users (username,password,admin) VALUES (:username,:password,:admin)"
            db.session.execute(sql, {"username":username, "password":hash_value, "admin":isadmin})
            db.session.commit()
        except:
            return False
        return login(username, password)
    return False

def check_registeration(username, password):
    if len(username) > 20 or len(username) < 3 or len(password) > 20 or len(password) < 6:
        return False
    return True

def username():
    return session.get("username",0)

def get_user_id(username):
    if username == 0:
        return False
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    return result.fetchone()

def is_admin():
    user = username()
    if user == 0:
        print("user 0 in is_admin, not logged in")
        return False
    sql = "SELECT admin FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":user})
    admin = result.fetchone()
    print("is admin?",admin)
    if admin[0] == True:
        return True
    return False

def is_logged_in():
    is_logged = username()
    print("is_logged: ", is_logged)
    if is_logged != 0:
        is_logged = get_user_id(is_logged)
        is_logged = is_logged[0]
        print("user_id: ", is_logged)
    return is_logged

def get_users_reviews(id):
    sql = "SELECT RV.id, RV.review, RV.score, RV.visited, RV.sent_at, RE.name FROM reviews RV, restaurants RE, users U WHERE RV.restaurant_id=RE.id AND RV.user_id=U.id AND U.id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()