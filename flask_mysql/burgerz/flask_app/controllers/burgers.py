
from flask_app import app #importing the app variable from the app package in __init__.py

from flask_app.models.burger import Burger #importing the Burger class from the burger.py file in the models folder

from flask import render_template, redirect, request, session, flash # type: ignore


@app.route('/')
def index():
    return render_template("index.html")

# gets all the burgers and returns them in a list of burger objects .
@app.route('/create',methods=['POST'])
def create():
    data = {
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    # if there are errors:
    # We call the staticmethod from the Burger model to validate
    if not Burger.validate_burger(data): #if the validate_burger method returns false
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    else:
        Burger.save(data)
        return redirect("/burgers")



# gets all the burgers and returns them in a list of burger objects .
@app.route('/burgers')
def burgers():
    return render_template("results.html",all_burgers=Burger.get_all())


@app.route('/show/<int:burger_id>')
def detail_page(burger_id):
    data = {
        'id': burger_id
    }
    return render_template("details_page.html",burger=Burger.get_one(data))

@app.route('/edit_page/<int:burger_id>')
def edit_page(burger_id):
    data = {
        'id': burger_id
    }
    return render_template("edit_page.html", burger = Burger.get_one(data))

@app.route('/update/<int:burger_id>', methods=['POST'])
def update(burger_id):
    data = {
        'id': burger_id,
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    Burger.update(data)
    return redirect(f"/show/{burger_id}")

@app.route('/delete/<int:burger_id>')
def delete(burger_id):
    data = {
        'id': burger_id,
    }
    Burger.destroy(data)
    return redirect('/burgers')