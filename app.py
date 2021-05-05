import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


# configuration
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# homepage
@app.route("/")
def index():
    recipes = list(mongo.db.recipes.find())
    return render_template("index.html", recipes=recipes)


# bia featured brands
@app.route("/bia_featured")
def bia_featured():
    brands = list(mongo.db.brands.find())
    return render_template("featured.html", brands=brands)


# individual brand page
@app.route("/brand/<brand_id>")
def brand(brand_id):
    # Find brand from id
    brand = mongo.db.brands.find_one({"_id": ObjectId(brand_id)})

    return render_template("brand.html", brand=brand)


# recipes
@app.route("/all_recipes")
def all_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


# search recipes
@app.route("/search", methods=["GET", "POST"])
def search():
    # Search for recipes based on query
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# signup
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# login
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
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# user profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        # Admin has acces to all recipes
        if session["user"] == "admin":
            user_recipes = list(mongo.db.recipes.find())
        else:
            # user sees own recipes
            user_recipes = list(
                mongo.db.recipes.find({"created_by": session["user"]}))
        return render_template(
            "users/profile.html", username=username, user_recipes=user_recipes)
    return redirect(url_for("login"))


# logout
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# individual recipe page
@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    # Find recipe from id
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    return render_template("recipe.html", recipe=recipe)


# add recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # Adding recipe to db
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "img_url": request.form.get("img_url"),
            "serves": request.form.get("serves"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "description": request.form.get("description"),
            "brand_name": request.form.get("brand_name"),
            "brand_url": request.form.get("brand_url"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe has been successfully added")
        return redirect(url_for("profile", username=session['user']))
    # Find categories in db
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


# Edit recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    # editing recipe to db
    if request.method == "POST":
        editing = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "img_url": request.form.get("img_url"),
            "serves": request.form.get("serves"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "description": request.form.get("description"),
            "brand_name": request.form.get("brand_name"),
            "brand_url": request.form.get("brand_url"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, editing)
        flash("Recipe has been successfully Updated")
        return redirect(url_for("profile", username=session['user']))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# delete recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # Remove recipe from db
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe has been successfully deleted")
    return redirect(url_for("profile", username=session['user']))


# categories
@app.route("/categories")
def categories():
    # Find categories in db
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# add categories
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        # Add category to db
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New category has been successfully added")
        return redirect(url_for("categories"))

    return render_template("add_category.html")


# edit categories
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        # Edit category from db
        editing = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, editing)
        flash("Category has been successfully edited")
        return redirect(url_for("categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# delete categories
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    # Remove category from db
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category has been successfully deleted")
    return redirect(url_for("categories"))


# run application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# change to False before submission
