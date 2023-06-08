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


@app.route('/users/new', methods=["POST"])
def create_user():
    #data = { 
        #"fname": request.form["fname"],
        #"lname" : request.form["lname"],
        # "email" : request.form["email"],
    #}
    User.save(request.form) #you could also pass the data dict instead of request.form values, which just seems like a lot of extra work to make a dict that is the same as request.form
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True, port=5007)