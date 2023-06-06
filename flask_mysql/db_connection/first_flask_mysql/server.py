from flask import Flask, render_template, request, redirect# Importing Flask to allow us to create our app,  #type: ignore
# import the class from friend.py
from friend import Friend
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends) # all_friends is the variable we will pass to index.html, and friends is the data we are sending to the template

@app.route('/friend/show/<int:friend_id>')
def show(friend_id):
    # calling the get_one method and supplying it with the id of the friend we want to get
    friend=Friend.get_one(friend_id)
    return render_template("show_friend.html", friend=friend)

@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string in our 'save' method in friend.py. for example, %(fname)s needs to match the key "fname" in the data dictionary.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    #request.form is another dictionary in python. It is a dictionary of all the data that was sent to the server from the form. The keys in request.form are the name attributes from the form inputs, and the values are the user's input.
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')


@app.route('/friends/update/<int:friend_id>',methods=['POST']) #this route is for updating a friend, and we are making sure to capture the id from the url. So to update a friend, we need to make sure we include <int:friend_id> in our route!
def update():
    Friend.update(request.form)
    return redirect('/')

@app.route('/friends/delete/<int:friend_id>') #this route is for deleting a friend, and we are making sure to capture the id from the url as well. So we need to make sure we include <int:friend_id> in our route!
def delete(friend_id):
    Friend.delete(friend_id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5007)

#where is the query_db method coming from? It is coming from the mysqlconnection.py file. We imported the function connectToMySQL from that file, and that function returns an instance of MySQLConnection, which has the query_db method available to it.