from flask import Flask, render_template  # Import Flask to allow us to create our app, this line is needed for every Flask app we make # type: ignore
app = Flask(__name__)    # Create a new instance of the Flask class called "app", also needed for every Flask app we make

@app.route('/')          # The "@" decorator associates this route with the function immediately following, which is hello_world()
def hello_world():
    return render_template("index.html", phrase= "hello", times=5) # Return the string 'Hello World!' as a response, we can also return HTML code with the render_template method and these variables

# DISCLAIMER: if port 5000 is not already in use, try using a different port number by adding the following to the end of the app.run() line:
#  for example: app.run(debug=True, host="localhost", port=5000)

# route is the decorator that tells Flask what URL should trigger our function

# it may show an error in the VSCode terminal, but it will still run the app, it shows an error because your import statement
# is not at the top of the file, but it will still run the app

# now lets add another route to our file, this will be a new function that will return a string

# import statements, maybe some other routes

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>/<bday>') # for a route '/hello/____/____' anything after '/hello/' gets passed as a variable 'name' and 'bday'
def hello(name, bday):             # when accessing the route, you'll need to include a name and bday varbiable in the url after '/hello/'
    print(name)
    print(bday)
    return f"Hello {name}, your birthday is {bday}. You're a baby!"

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5,6,2], students = student_info) # here we are creating a variable called random_numbers that we can use in our template and passing a list of numbers to it
# we are also passing a list of dictionaries called students to our template, which we'll be looping through in our template


if __name__=="__main__":   # IMPORTANT! This ensures this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode. If the local server is not running, this will start it for you. 
# If it is running, this will restart it. This is a great way to debug your code, 
# as it will automatically restart the server every time you save your code. 
# You can also  restart the server by pressing Ctrl + C in the terminal where it is running.

# app.run(debug=True) should be the very last statement! exit
