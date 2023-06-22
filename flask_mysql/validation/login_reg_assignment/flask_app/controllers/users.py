from flask_app import app #importing the app variable from the __init__.py file to run the server
from flask_bcrypt import Bcrypt #importing Bcrypt from flask_bcrypt to hash passwords # type: ignore
bcrypt = Bcrypt(app) #we are setting the variable bcrypt to Bcrypt(app) so that we can use bcrypt to hash passwords
from flask import flash, redirect, render_template, request, session, url_for #type: ignore
from flask_app.models.user import User #importing the User class from the user.py file in the models folder

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    data = { # next time we can just use request.form to get the data from the form bc the keys in the form = the data dictionary keys , and its less steps
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "password" : request.form["password"],
        "confirm_password" : request.form["confirm_password"],
        "bday" : request.form["bday"]
    }
    if not User.validate_reg(data): 
        return redirect("/")
    else:
        pw_hash = Bcrypt(app).generate_password_hash(data["password"]) #we are hashing the password here from the form
        data["password"] = pw_hash #we are setting the password in the data dictionary to the hashed password
        user_id = User.save(data)
        session["user_id"] = user_id #we are setting the session user_id to the user_id that is returned from the save method to log the user in after they register
        return redirect (url_for('success', id = session["user_id"])) #here we are redirecting to the success page and passing in the id of the user that was just created with the session user_id
    

@app.route("/success/<int:id>")
def success(id):
    if "user_id" not in session:
        flash("Please log in")
        return redirect("/")
    data = {
        "id": id
    }
    user = User.get_one(data) #we are getting the user from the database here by passing in the data dictionary with the id of the user that was just created
    return render_template("user_page.html", user = user)

@app.route("/login", methods=["POST"])
def login():
    data = {
        "email" : request.form["email"],
    }
    user = User.get_by_email(data)
    if not user:
        flash("Invalid Email/Password", 'log')
        return redirect("/")
    
    elif not bcrypt.check_password_hash(user.password, request.form["password"]): #we are checking the password here by passing in the hashed password from the database and the password from the form
        flash("Invalid Email/Password", 'log')
        return redirect("/")
    else:
        session["user_id"] = user.id # type: ignore #we are setting the session user_id to the user_id that is returned from the get_by_email method to log the user in after they register
        return redirect (url_for('success', id = session["user_id"]))

@app.route("/logout")
def logout():
    session.clear() #we are clearing the session here to log the user out
    return redirect("/")