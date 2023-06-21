#this is the init file, this is where we will import Flask and create our app.
#The main purpose of this file is to initialize our app and bring together all of the various routes and models we may create.


# Import Flask to allow us to create our app
from flask import Flask # type: ignore
from flask import session # type: ignore #this is for sessions, we use this to encrypt our session, and its also necesarry for flash messages
# Create a new instance of the Flask class called "app"
app = Flask(__name__)

app.secret_key = "shhhhhh" #this is for sessions, we use this to encrypt our session