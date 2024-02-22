from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = { "username": "Namgoo" }
    posts = [
        {
            "author": { "userame": "Namgoo" },
            "body": "Beautiful day in Portland!"
        },
        {
            "author": { "userame": "Namgoo" },
            "body": "Beautiful day in Portland!"
        },
    ]
    return render_template("index.html", user=user, posts=posts)