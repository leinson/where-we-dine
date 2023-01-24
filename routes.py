from flask import redirect, render_template, request
from app import app
import reviews


@app.route("/")
def index():
    list = reviews.get_reviews()
    return render_template("index.html", count=len(list), reviews=list)
