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

# Structure and most of the python code taken from CI walkthrough project -
# Task Manager and edited slightly
app = Flask(__name__)

# MondoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
# Home Page route
@app.route("/home")
def home():
    return render_template("index.html")


# All Habits Page route. Gets habits from db & searches for public habits
@app.route("/get_habits", methods=["GET", "POST"])
def get_habits():
    habits = list(mongo.db.habits.find({'is_public': True}))
    print('habits ', habits)
    if request.method == "POST":
        search_value = request.form.get("search_value")
        habits = list(mongo.db.habits.find({"$and": [{'habit_name': {
            '$regex': search_value}}, {'is_public': True}]}))

    content = {'habits': habits, 'welcome_message':
               'Your Future Habits Await!'}
    return render_template("habits.html", content=content)


# Sign Up Page route. Checks if username already in db & inserts new user
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

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful!")
    return render_template("signup.html")


# Log In Page route. Checks if username & password already in db
# and redirects existing user to My Habits Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()

            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username is not in the db
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

        return redirect(url_for("habits", username=session['user']))

    return render_template("login.html")


# My Habits Page route (re-uses habits.html, but with diff content).
# Progress functionality
@app.route("/habits/<username>", methods=["GET", "POST"])
def habits(username):
    # Take the session user's username from db and link it to My Habits page
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    habits = list(mongo.db.habits.find({'created_by': username}))
    print('habits', habits)
    # Search in My Habits for user's habits only
    if request.method == "POST":
        search_value = request.form.get("search_value")
        habits = list(mongo.db.habits.find({"$and": [{'habit_name': {
            '$regex': search_value}}, {'created_by': username}]}))
    for habit in habits:
        progress_list = list(mongo.db.progress.find(
            {'habit_id': habit['_id']}))
        habit['progress_list'] = progress_list
    print('habits with progress ', habits)
    if session["user"]:
        content = {
            'habits': habits, 'welcome_message': 'Welcome %s' % username,
            'my_habits': True}
        return render_template("habits.html", content=content)


# Log Out route
@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Add Habit Page route
# Add habit with input fields from MongoDB & incert into My Habits
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
        # Incert new habit & notify of successful action
        mongo.db.habits.insert_one(habit)
        flash("Habit Successfully Added")
        return redirect(url_for("habits", username=session['user']))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_habit.html", categories=categories)


# Add Habit Progress route on My Habits Page
@app.route("/add_habit_progres", methods=["POST"])
def add_habit_progress():
    if request.method == "POST":
        print('Completion 2 ', request.form.getlist("completion_time[]"))
        # Display progress in description once user clicks Done button
        progress = {
            "habit_id": ObjectId(request.form.get("habit_id")),
            "completion_time": request.form.getlist("completion_time"),
            "progess_date": datetime.datetime.now()
        }

        mongo.db.progress.insert_one(progress)
        flash("Progress Successfully Added")
        return redirect(url_for("habits", username=session['user']))


# Edit Habit Page route.
# Request prefilled form by habit's ID for editing or cloning
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
        action_name = request.form.get("action_name")
        # Update habit if user editing their own
        if action_name == 'Updated':
            mongo.db.habits.update({"_id": ObjectId(habit_id)}, submit)
        # Clone & insert public habit to My Habits Page
        if action_name == 'Cloned':
            mongo.db.habits.insert_one(submit)
        flash("Habit Successfully %s" % action_name)
        return redirect(url_for("habits", username=session['user']))

    habit = mongo.db.habits.find_one({"_id": ObjectId(habit_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_habit.html", habit=habit, categories=categories,
        action_message='Edit', action_name='Updated')


# Clone Habit Page route.
# Re-use edit page, but clone wording and instead
@app.route("/clone_habit/<habit_id>", methods=["GET"])
def clone_habit(habit_id):
    habit = mongo.db.habits.find_one({"_id": ObjectId(habit_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_habit.html", habit=habit, categories=categories,
        action_message='Clone', action_name='Cloned')


# Delete Habit route.
# Remove habit from db
@app.route("/delete_habit/<habit_id>")
def delete_habit(habit_id):
    mongo.db.habits.remove({"_id": ObjectId(habit_id)})
    flash("Habit Successfully Deleted")
    return redirect(url_for("habits", username=session['user']))


# Manage Categories Page route.
# Gets categories from db
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# Add Category Page route.
# Incert new category into Manage Categories Page
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# Edit Category Page route.
# Request pre-filled category name by category's ID for editing
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# Delete category route.
# Remove category from db
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
