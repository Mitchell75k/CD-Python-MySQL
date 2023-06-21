
from flask_app.controllers import users #importing the users controller file, you must import the controller file so that the routes in the controller file will be registered with the server


from flask_app import app #importing the app variable from the __init__.py file to run the server

if __name__=="__main__":
    app.run(debug=True, port=5010)