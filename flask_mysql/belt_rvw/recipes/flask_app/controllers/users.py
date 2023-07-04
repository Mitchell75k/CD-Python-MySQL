from flask_app import app #importing the app variable from the __init__.py file to run the server
from flask_bcrypt import Bcrypt #importing Bcrypt from flask_bcrypt to hash passwords # type: ignore
bcrypt = Bcrypt(app) #we are setting the variable bcrypt to Bcrypt(app) so that we can use bcrypt to hash passwords
from flask import flash, redirect, render_template, request, session, url_for #type: ignore
from flask_app.models.user import User #importing the User class from the user.py file in the models folder
from flask_app.models.recipe import Recipe #importing the Recipe class from the recipe.py file in the models folder

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/register", methods=["POST"])
def register():
    data = { 
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "password" : request.form["password"],
        "confirm_password" : request.form["confirm_password"],
    }
    if not User.validate_reg(data): 
        return redirect("/")
    else:
        pw_hash = Bcrypt(app).generate_password_hash(data["password"]) 
        data["password"] = pw_hash 
        user_id = User.save(data)
        session["user_id"] = user_id 
        return redirect (url_for('success', id = session["user_id"])) 
    

@app.route("/success/<int:id>")
def success(id):
    if "user_id" not in session:
        flash("Please log in")
        return redirect("/")
    data = {
        "id": id
    } 
    return render_template("user_page.html", user = User.get_by_id(data), recipes = Recipe.get_all_recipes_with_chef())

@app.route("/login", methods=["POST"])
def login():
    data = {
        "email" : request.form["email"],
    }
    user = User.get_by_email(data)
    if not user:
        flash("Invalid Email/Password", 'log')
        return redirect("/")
    
    elif not bcrypt.check_password_hash(user.password, request.form["password"]): 
        flash("Invalid Email/Password", 'log')
        return redirect("/")
    else:
        session["user_id"] = user.id 
        return redirect (url_for('success', id = session["user_id"]))


@app.route("/logout")
def logout():
    session.clear() 
    return redirect("/")