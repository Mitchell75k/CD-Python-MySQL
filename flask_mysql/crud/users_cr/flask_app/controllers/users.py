
from flask_app import app #importing the app variable from the __init__.py file to run the server
from flask_app.models.user import User #importing the User class from the user.py file in the models folder

from flask import render_template, redirect, request, session, flash, url_for  # type: ignore


@app.route("/")
def index():
    return render_template("create.html") 


@app.route('/users')
def users():
    users = User.get_all()
    print(f"users:{users}")
    return render_template("read_all.html", all_users = users)


@app.route('/users/<int:id>')
def show_user(id):
    data = {
        "id" : id #we use data because we are using a dictionary to pass the id into the get_one method
    }
    user = User.get_one(data)
    print(f"user:{user}")
    return render_template("read_one.html", user = user)



@app.route('/users/new', methods=["POST"])
def create_user():
    #data = { 
    #    "fname": request.form["fname"],
    #    "lname" : request.form["lname"],
    #    "email" : request.form["email"],
    #}
    User.save(request.form) #you could also pass the data dict instead of request.form values, which just seems like a lot of extra work to make a dict that's the same as request.form
    return redirect('/users')


@app.route('/users/<int:id>/update', methods=["POST"])
def update_user(id):
    data = {
        "id" : id,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
    }
    User.update(data)
    return redirect((url_for('show_user', id=id))) #notes:

# "redirect('/users/<int:id>')" was not working because the redirect is not passing the id into the show_user function, so it's not finding the user to display
# to pass the id into the show_user function, we need to use the url_for function in the redirect like so: return redirect(url_for('show_user', id=id))
# url_for is a function that takes the name of a function as a string and any arguments that function takes, and returns the url for that function by replacing the arguments in the url with the arguments passed into the url_for function
# but first, we need to import url_for from flask 


@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {
        "id" : id
    }
    user = User.get_one(data)
    return render_template("update.html", user = user)


@app.route('/users/<int:id>/delete')
def delete_user(id):
    data = {
        "id" : id
    }
    User.delete(data)
    return redirect('/users')