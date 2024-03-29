from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template("login.html", title="Sign In", form=form)