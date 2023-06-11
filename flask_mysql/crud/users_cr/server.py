from flask import Flask, render_template, request, redirect # Importing Flask to allow us to create our app,  #type: ignore
# import the class from user.py
from user import User
app = Flask(__name__)

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
        #"fname": request.form["fname"],
        #"lname" : request.form["lname"],
        # "email" : request.form["email"],
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
    return redirect('/users') #figure out how to redirect to the user's page instead of the index page after updating


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


if __name__ == "__main__":
    app.run(debug=True, port=5007)