from flask_app.controllers import authors, books

from flask_app import app #importing the app variable from the __init__.py file to run the server

if __name__=="__main__":
    app.run(debug=True, port=5006)