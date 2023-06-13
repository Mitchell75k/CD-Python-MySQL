from flask_app import app #importing the app variable from the flask_app package
from flask_app.models.dojo import Dojo #importing the Dojo class from the dojo.py file in the models folder

from flask import render_template, redirect, request, session, flash, url_for  # type: ignore

@app.route("/")
def index():
    return render_template("dojos.html")

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(f"dojos:{dojos}")
    return render_template("dojos.html", all_dojos = dojos)

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        "id" : id #we use data because we are using a dictionary to pass the id into the get_one method
    }
    dojo = Dojo.get_one(data)
    print(f"dojo:{dojo}")
    return render_template("show_dojo.html", dojo = dojo)

@app.route('/dojos/new', methods=["POST"])
def create_dojo():
    Dojo.save(request.form)  #using request.form instead of data dict because request.form is already a dict, just make sure the keys match the column names in the table
    return redirect('/dojos')




#NEXT STEPS: 
# 1. add a form to the dojos.html page to create a new dojo
# 2. finish form on the new_ninja.html page to create a new ninja
# 3. make a new ninja controller and add routes to it to create a new ninja and to show a ninja
# 4. add a route to the dojos controller to delete a dojo
# 5. add a route to the dojos controller to delete a ninja


