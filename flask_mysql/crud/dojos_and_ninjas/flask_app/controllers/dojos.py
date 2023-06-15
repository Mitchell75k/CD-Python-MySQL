from flask_app import app #importing the app variable from the flask_app package
from flask_app.models.dojo import Dojo #importing the Dojo class from the dojo.py file in the models folder
from flask_app.models.ninja import Ninja #importing the Ninja class from the ninja.py file in the models folder

from flask import render_template, redirect, request, session, flash, url_for  # type: ignore


@app.route('/')
def dojos():
    dojos = Dojo.get_all()
    print(f"dojos:{dojos}")
    return render_template("dojos.html", all_dojos = dojos)

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        "id" : id #we use data because we are using a dictionary to pass the id into the get_one method
    }
    dojo_w_ninjas= Dojo.get_dojo_with_ninjas(data)
    print(f"dojo:{dojo_w_ninjas}")
    return render_template("show_dojo.html", dojo = dojo_w_ninjas)


@app.route('/dojos/new', methods=["POST"])
def create_dojo():
    Dojo.save(request.form)  #using request.form instead of data dict because request.form is already a dict, just make sure the keys match the column names in the table
    return redirect('/')

@app.route('/dojos/<int:id>/delete') 
def delete_dojo(id):
    data = {
        "id" : id
    }
    Dojo.delete(data)
    return redirect('/')

@app.route('/dojos/<int:id>/edit')
def edit_dojo(id):
    data = {
        "id" : id
    }
    dojo = Dojo.get_one(data)
    return render_template("edit_dojo.html", dojo = dojo)

@app.route('/dojos/<int:id>/update', methods=["POST"])
def update_dojo(id):
    data = {
        "id" : id,
        "name" : request.form["name"]
    }
    Dojo.update(data)
    return redirect('/')


#NINJA ROUTES- couldnt get the ninja routes to work in its own controller, so I just put the ninja routes in the dojos controller
@app.route("/create/ninja") 
def ninjas():
    dojos = Dojo.get_all()
    return render_template("new_ninja.html", all_dojos = dojos) #we are going to use all_dojos in the new_ninja.html file to populate the dropdown menu with all the dojos by looping through it


@app.route("/ninjas/new", methods=["POST"])
def create_ninja():
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]
    }
    Ninja.save(data)
    return redirect(url_for('show_dojo', id=request.form["dojo_id"]))


@app.route('/ninjas/<int:id>/delete')
def delete_ninja(id):
    data = {
        "id" : id
    }
    Ninja.delete(data)
    referer=request.headers.get("Referer") #this gets the url of the page that the delete button was clicked on so we can redirect back to that page
    Ninja.delete(data)
    return redirect(referer)#request.headers.get refers to the url of the page that the delete button was clicked on


@app.route('/ninjas/<int:id>/edit')
def edit_ninja(id):
    data = {
        "id" : id
    }
    ninja = Ninja.get_one(data)
    dojos = Dojo.get_all() #we need to get all the dojos so we can display them in the dropdown menu to let the user select a new dojo for the ninja
    return render_template("edit_ninja.html", ninja = ninja, all_dojos = dojos) #ninja will be used to prepopulate the form with the ninjas current info


@app.route('/ninjas/<int:id>/update', methods=["POST"]) #this route updates the ninja just like the create ninja route, but we need to pass in the id so we know which ninja to update
def update_ninja(id):
    data = {
        "id" : id,
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]
    }
    Ninja.update(data) #create the update method in the Ninja model next
    return redirect(url_for('show_dojo', id=request.form["dojo_id"])) #this redirects to the show_dojo route in the dojos controller, which will display the dojo that the ninja belongs to
# the id variable in the url_for function is the id of the dojo that the ninja belongs to, so we can display the dojo that the ninja belongs to after updating the ninja