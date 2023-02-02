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

def is_admin():
    user = username()
    if user == 0:
        print("user 0")
        return False
    sql = "SELECT admin FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":user})
    admin = result.fetchone()
    print("is admin?",admin)
    if admin[0] == True:
        return True
    return False