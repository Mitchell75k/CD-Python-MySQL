
from flask import Flask  # Import Flask to allow us to create our app, this line is needed for every Flask app we make  # type: ignore
app = Flask(__name__)    # Create a new instance of the Flask class called "app", also needed for every Flask app we make

@app.route('/')          # The "@" decorator associates this route with the function immediately following, which is hello_world()
def hello_world():
    return "Hello World!"  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo!'  # Return the string 'Dojo!' as a response

@app.route('/say/<string:name>')
def say_hi(name):
    print (name)
# if name is an integer, return an error message
    if name.isnumeric(): 
        return "ERROR 404: Sorry! No response. Please enter non-numerical values only."
    else: 
        return f"Hi {name}!" # Return the string 'Hi' as a response and the name input in the url

@app.route('/repeat/<string:word>/<int:num>') # this route will take in a word and a number and print the word that many times
def repeat(word, num):
    print (word)
    print (num)
    return f"{word} " * num

@app.errorhandler(404) # This is the route to handle errors, it takes in a parameter for the type of error
def page_not_found(e):
    return "ERROR 404: Sorry! No response. Please try again."

if __name__=="__main__":   # IMPORTANT! This ensures this file is being run directly and not from a different module 
    app.run(debug=True, host="localhost", port=5001)