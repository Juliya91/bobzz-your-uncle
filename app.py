import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# mondodb
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_habits")
def get_habits():
    habits = list(mongo.db.habits.find({'is_public': True}))
    print('habits ', habits)
    return render_template("habits.html", habits=habits)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(signup)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful!")
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

        return redirect(url_for("habits", username=session['user']))

    return render_template("login.html")


@app.route("/habits/<username>", methods=["GET", "POST"])
def habits(username):
    # Take the session user's username from db and link it to My Habits page
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    habits = list(mongo.db.habits.find({'created_by': username}))
    print('habits', habits)
    for habit in habits:
        progress_list = list(mongo.db.progress.find(
            {'habit_id': habit['_id']}))
        habit['progress_list'] = progress_list
    print('habits with progress ', habits)
    if session["user"]:
        return render_template("habits.html", habits=habits)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_habit", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habit = {
            "category_name": request.form.get("category_name"),
            "habit_name": request.form.get("habit_name"),
            "habit_description": request.form.get("habit_description"),
            "completion_time": request.form.get("completion_time"),
            "created_by": session["user"]
        }

        mongo.db.habits.insert_one(habit)
        flash("Habit Successfully Added")
        return redirect(url_for("habits", username=session['user']))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_habit.html", categories=categories)


@app.route("/add_habit_progres", methods=["POST"])
def add_habit_progress():
    if request.method == "POST":
        print('Completion 2 ', request.form.getlist("completion_time[]"))
        progress = {
            "habit_id": ObjectId(request.form.get("habit_id")),
            "completion_time": request.form.getlist("completion_time"),
            "progess_date": datetime.datetime.now()
        }

        mongo.db.progress.insert_one(progress)
        flash("Progress Successfully Added")
        return redirect(url_for("habits", username=session['user']))


@app.route("/edit_habit/<habit_id>", methods=["GET", "POST"])
def edit_habit(habit_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "habit_name": request.form.get("habit_name"),
            "habit_description": request.form.get("habit_description"),
            "completion_time": request.form.get("completion_time"),
            "created_by": session["user"]
        }

        mongo.db.habits.update({"_id": ObjectId(habit_id)}, submit)
        flash("Habit Successfully Updated")

    habit = mongo.db.habits.find_one({"_id": ObjectId(habit_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_habit.html", habit=habit, categories=categories)


@app.route("/delete_habit/<habit_id>")
def delete_habit(habit_id):
    mongo.db.habits.remove({"_id": ObjectId(habit_id)})
    flash("Habit Successfully Deleted")
    return redirect(url_for("habits", username=session['user']))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
