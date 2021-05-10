import os
import uuid
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
@app.route("/bia_brands")
def bia_brands():
    brands = list(mongo.db.brands.find())
    return render_template("bia_brands.html", brands=brands)


# individual brand page
@app.route("/brand/<brand_id>")
def brand(brand_id):
    # Find brand from id
    brand = mongo.db.brands.find_one({"_id": ObjectId(brand_id)})

    # Show 404 if recipe id doesn't exist
    if not recipe:
        return render_template("errors/404.html")

    recipes = list(mongo.db.recipes.find())
    return render_template("brand.html", brand=brand, recipes=recipes)


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

        # put the new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("users/register.html")


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

    return render_template("users/login.html")


# user profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Only users can access profile
    if not session.get("user"):
        return render_template("errors/404.html")

    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        # Admin has access to all recipes
        if session["user"] == "admin":
            user_recipes = list(mongo.db.recipes.find())
        else:
            # user views own recipes
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


@app.route("/recipes/<category>")
def recipes(category):
    # Show recipes by category
    if category == "all":
        recipes = list(mongo.db.recipes.find())
    elif category == "breakfast":
        recipes = list(mongo.db.recipes.find({"category_name": "Breakfast"}))
    elif category == "dinner":
        recipes = list(mongo.db.recipes.find({"category_name": "Dinner"}))
    elif category == "dessert":
        recipes = list(mongo.db.recipes.find({"category_name": "Dessert"}))
    elif category == "vegan":
        recipes = list(mongo.db.recipes.find({"category_name": "Vegan"}))

    return render_template(
        "recipes.html", recipes=recipes, category=category)


# individual recipe page
@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    # Find recipe from id
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # Show 404 if recipe id doesn't exist
    if not recipe:
        return render_template("errors/404.html")

    return render_template("recipe.html", recipe=recipe)


# add recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # Only logged in users can add recipes
    if not session.get("user"):
        return render_template("errors/404.html")

    # Adding recipe to db
    if request.method == "POST":
        result = None

        # add image to database
        if 'item_image' in request.files:
            item_image = request.files['item_image']
            if item_image.filename != '':
                # generate filename using an uuid
                item_image.filename = str(uuid.uuid4())
                result = mongo.save_file(item_image.filename, item_image)

        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "img_url": request.form.get("img_url"),
            'item_image': item_image.filename,
            "serves": request.form.get("serves"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "description": request.form.get("description"),
            "brand_name": request.form.get("brand_name"),
            "brand_url": request.form.get("brand_url"),
            "created_by": session["user"],
            'img_id': result
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe has been successfully added")
        return redirect(url_for("profile", username=session["user"]))
    # Find categories in db
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


# retrieve images from mongoDB
@app.route('/img_uploads/<filename>')
def img_uploads(filename):
    return mongo.send_file(filename)


# Edit recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    # Only logged in users can edit recipes
    if not session.get("user"):
        return render_template("errors/404.html")

    # editing recipe to db
    if request.method == "POST":
        result = None
        # check if new image selected
        if 'item_image' in request.files:
            item_image = request.files['item_image']
            if item_image.filename == '':
                item_image.filename = request.form.get('item_image_up')
            else:
                # if new image selected delete old from mongoDB
                recipe = mongo.db.recipes.find_one_or_404(
                    {"_id": ObjectId(recipe_id)})
                img_id = recipe["img_id"]
                if img_id:
                    files_id = mongo.db.fs.files.find_one_or_404(
                        {"_id": img_id})["_id"]
                    mongo.db.fs.chunks.remove({"files_id": ObjectId(files_id)})
                    mongo.db.fs.files.remove({"_id": ObjectId(img_id)})

                # generate filename using an uuid
                item_image.filename = str(uuid.uuid4())
                result = mongo.save_file(item_image.filename, item_image)

        editing = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "img_url": request.form.get("img_url"),
            'item_image': item_image.filename,
            "serves": request.form.get("serves"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "description": request.form.get("description"),
            "brand_name": request.form.get("brand_name"),
            "brand_url": request.form.get("brand_url"),
            "created_by": session["user"],
            'img_id': result
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, editing)
        flash("Recipe has been successfully Updated")
        return redirect(url_for("profile", username=session["user"]))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# delete recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # check if recipe has image
    recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    img_id = recipe["img_id"]

    if img_id:
        files_id = mongo.db.fs.files.find_one_or_404(
            {"_id": img_id})["_id"]
        mongo.db.fs.chunks.remove({"files_id": ObjectId(files_id)})
        mongo.db.fs.files.remove({"_id": ObjectId(img_id)})

    # Remove recipe from db
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe has been successfully deleted")
    return redirect(url_for("profile", username=session["user"]))


# manage categories
@app.route("/categories")
def categories():
    # Only the admin user can manage categories
    if not session.get("user") == "admin":
        return render_template("errors/404.html")

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


# manage brands
@app.route("/manage_brands")
def manage_brands():
    # Only the admin user can manage brands
    if not session.get("user") == "admin":
        return render_template("errors/404.html")

    # Find brands in db
    brands = list(mongo.db.brands.find().sort("brand_name", 1))
    return render_template("manage_brands.html", brands=brands)


# add brand
@app.route("/add_brand", methods=["GET", "POST"])
def add_brand():
    # Only the admin user can add brands
    if not session.get("user") == "admin":
        return render_template("errors/404.html")

    # Adding brand to db
    if request.method == "POST":

        brand = {
            "brand_name": request.form.get("brand_name"),
            "brand_description": request.form.get("brand_description"),
            "brand_url": request.form.get("brand_url"),
            "brand_img": request.form.get("brand_img")
        }

        mongo.db.brands.insert_one(brand)
        flash("New brand has been successfully added")
        return redirect(url_for("manage_brands"))
    # Find recipe brands in db
    recipes = mongo.db.recipes.find().sort("brand_name", 1)
    return render_template("add_brand.html", recipes=recipes)


# Edit brands
@app.route("/edit_brand/<brand_id>", methods=["GET", "POST"])
def edit_brand(brand_id):
    # Only the admin user can edit brands
    if not session.get("user") == "admin":
        return render_template("errors/404.html")

    # updating brand to db
    if request.method == "POST":

        updating = {
            "brand_name": request.form.get("brand_name"),
            "brand_description": request.form.get("brand_description"),
            "brand_url": request.form.get("brand_url"),
            "brand_img": request.form.get("brand_img")
        }
        mongo.db.brands.update({"_id": ObjectId(brand_id)}, updating)
        flash("Brand has been successfully Updated")
        return redirect(url_for("manage_brands"))

    brand = mongo.db.brands.find_one({"_id": ObjectId(brand_id)})
    recipes = mongo.db.recipes.find().sort("brand_name", 1)
    return render_template("edit_brand.html", brand=brand, recipes=recipes)


# delete brands
@app.route("/delete_brand/<brand_id>")
def delete_brand(brand_id):
    # Remove brand from db
    mongo.db.brands.remove({"_id": ObjectId(brand_id)})
    flash("Brand has been successfully deleted")
    return redirect(url_for("manage_brands"))


# CUSTOM ERROR HANDLERS
# 404 Error - Page not found
@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


# 500 Error - Internal Server Error
@app.errorhandler(500)
def internal_server(error):
    return render_template("errors/500.html"), 500


# RUN APPLICATION
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# change to False before submission
