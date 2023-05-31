from flask import Flask, render_template, request, redirect, session # request and redirect are needed for POST routes. Session is needed for session variables. render_template is needed to render the html templates #type: ignore
app = Flask(__name__)
app.secret_key = "ThisIsSecret" # you need to set a secret key for security purposes when using session variables

# our index route will handle rendering our form
@app.route('/') # notice that we are only handling the GET request on this route by default since we are rendering a template and not processing any data
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST']) # notice we defined which HTTP methods are allowed by this route, this is optional because the default is GET. We never want to make a POST request to the index route because that is where we are rendering our form.
def create_user(): # the server is listening for a POST request to the '/users' route and will fire the create_user function when it receives one
    print("Got Post Info")
    
    print(request.form) # request.form is a dictionary that contains the data that was submitted in the form in the index.html file 
    
    session['username'] = request.form['name'] # we can access the data in the dictionary by the name attribute that we gave each input in the html form, example: name = request.form['name'], email = request.form['email']
    session ['useremail'] = request.form['email'] 
    #instead, we are storing the data from the form in session variables so that we can access the data in the show.html template without having to pass the data to the template as a variable
    # session variables are accessible in any route function, just like request.form is accessible in any route function. The difference is that session variables are accessible in the template as well, while request.form is not.
    
    return redirect("/show") # redirecting to the '/show' route so that we can display the information from the form on the show.html page since we don't want to display the information from the form on the index.html page
    
    # Never render a template on a POST request. this will cause a refresh to re-add the user to our database
    #instead we will redirect to our show route and then render the template, this way a refresh will not re-add the user to our database


#NOTE:  note that the type of anything that comes in through request.form will be a "string" no matter what. If you want that value to be identified as an actual number you'll have to type cast it.
# for example: request.form['age'] will be a string, so if you want to use that value as an integer you'll have to do something like this: age = int(request.form['age'])

@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template('show.html', name_on_template = session['username'], email_on_template = session['useremail']) 
# we are rendering the show.html template and passing the name and email variables to the template for it to display the information from the form
# we could also pass the session variables directly to the template like this: return render_template('show.html', name_on_template = request.form['name'], email_on_template = request.form['email'])
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)

