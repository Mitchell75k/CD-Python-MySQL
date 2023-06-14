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


#NINJA ROUTES- couldnt get the ninja routes to work in its own controller, so I just put the ninja routes in the dojos controller
@app.route("/create/ninja") 
def ninjas():
    dojos = Dojo.get_all()
    return render_template("new_ninja.html", all_dojos = dojos)


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
    #if request.form["dojo_id"] == None:
        #return redirect('/')
    #return redirect(url_for('show_dojo', id=request.form["dojo_id"])) FIGURE OUT L8R
    return redirect('/')







