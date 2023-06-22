from flask_app.config.mysqlconnection import connectToMySQL #importing the function from the mysqlconnection.py file in the config folder
from flask import flash #type: ignore
from flask_app import app #importing the app variable from the __init__.py file to run the server

from flask_bcrypt import Bcrypt        #importing Bcrypt from flask_bcrypt to hash passwords #type: ignore
bcrypt = Bcrypt(app)                   #bcrypt = Bcrypt(app) is creating an instance of Bcrypt and passing in the app variable from the __init__.py file

import re #importing re to use regular expressions
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #this is the regular expression for emails

DB = 'login_reg'
class User:
    def __init__(self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name  = data['last_name']
        self.email = data['email']
        self.password = data['password'] #we are gettin
        self.bday = data['birthdate']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , password , birthdate , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , %(password)s , %(bday)s , NOW() , NOW() );"
        return connectToMySQL(DB).query_db( query, data )
    
    @classmethod
    def get_one(cls, data ):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        return cls( results[0] ) # type: ignore
    
    @classmethod
    def get_by_email(cls, data ):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query, data)
        if len(results) < 1:  #type: ignore #if the email is not in the database, return false
            return False
        return cls( results[0] ) # type: ignore 
    
    @staticmethod
    def validate_reg(user): #we are passing in the request.form from the controller to validate the user
        is_valid = True
        if len(user['fname']) < 3:
            flash("First name must be at least 3 characters.", 'reg') #the second argument is the category of the flash message, which is 'reg' for registration
            print("First name must be at least 3 characters.")
            is_valid = False
        
        if len(user['lname']) < 3:
            flash("Last name must be at least 3 characters.", 'reg')
            print("Last name must be at least 3 characters.")
            is_valid = False
        
        if not EMAIL_REGEX.match(user['email']): #if the email doesn't match the regex
            flash("Invalid email address!" , 'reg')
            print("Invalid email address!")
            is_valid = False
        
        if len(user['password']) < 4:
            flash("Password must be at least 8 characters." , 'reg')
            print("Password must be at least 8 characters.")
            is_valid = False
        
        if user['password'] != user['confirm_password']: #confirm_password is the name of the input field in the registration form
            flash("Passwords do not match." , 'reg') 
            print("Passwords do not match.")
            is_valid = False
        
        if not user['bday']: #if the birthdate is empty
            flash("Please enter a birthdate." , 'reg')
            print("Please enter a birthdate.")
            is_valid = False
        
        if user['bday'] > '2013-06-21': #if the birthdate is after 2013-06-21, meaning they are less than 10 years old, they cannot register
            flash("You must be at least 10 years old to register, kiddo." , 'reg')
            print("You must be at least 10 years old to register, kiddo.")
            is_valid = False
        return is_valid

#FAILED ATTEMPT AT LOGIN VALIDATION- It was not working bc the password was not being hashed in the database, so it was not matching the hashed password in the database. 
#it was pretty unnecessary to do this anyway, since we are using flask_bcrypt to hash the password in the controller, and then we are just checking the password in the controller

#    @staticmethod
#    def validate_login(user): #user refers to request.form from the controller, as well as the data dictionary in the controller
#        is_valid = True
#        #the password is not correct, return false
#        if not bcrypt.check_password_hash(user['password']):
#            flash("Incorrect password." , 'log')
#            print("Incorrect password.")
#            return False
#        
#        #if the email is not in the database, return false
#        if not User.get_by_email({'email': user['email']}):
#            flash("Email not found." , 'log')
#            print("Email not found.")
#            is_valid = False
#        
#        return is_valid