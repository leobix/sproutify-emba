from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user

from .models import User
from . import db

auth = Blueprint("auth", __name__)

default_password = "password"


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    # password = request.form.get("password")

    # no password required
    password = default_password

    # remember = True if request.form.get("remember") else False
    # Always remember the user
    remember = True

    user = User.query.filter_by(email=email).first()

    if not user:
        user = User(
            email=email,
            password=generate_password_hash(password, method="scrypt"),
        )

        db.session.add(user)
        db.session.commit()

    login_user(user, remember=remember)
    return redirect(url_for("main.instructions"))


@auth.route("/signup")
def signup():
    return render_template("signup.html")


@auth.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    name = request.form.get("name")
    # password = request.form.get("password")

    # no password required
    password = default_password

    user = User.query.filter_by(email=email).first()

    if user:
        flash("Email address already exists")
        return redirect(url_for("auth.signup"))

    new_user = User(
        email=email,
        name=name,
        password=generate_password_hash(password, method="scrypt"),
    )

    db.session.add(new_user)
    db.session.commit()

    # login and redirect to profile
    login_user(new_user, remember=True)
    return redirect(url_for("main.profile"))

    # redirect to the login page
    # return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
