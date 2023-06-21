from flask_app.config.mysqlconnection import connectToMySQL #importing the function that will return an instance of a connection

from flask import flash # type: ignore #importing flash to use flash messages

import re #importing regex for email validation

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$') #regex for email validation

# model the class after the users table from our database
class User:
    DB = 'users_schema'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name  = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    # class methods to get all users from the database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results: # type: ignore
            users.append( cls(user) )
        return users
    
    # class method to get a user from the database
    @classmethod
    def get_one(cls, data ):
        query = "SELECT * FROM users WHERE id = %(id)s;" #%(id)s is a placeholder for the id we will get from the data dictionary we pass into the method from server.py
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls( results[0] ) # type: ignore
    
    # class method to add/save a user to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL(cls.DB).query_db( query, data )
    
    # class method to update a user in the database
    @classmethod
    def update(cls, data ):
        query = "UPDATE users SET first_name = %(fname)s , last_name = %(lname)s , email = %(email)s , updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db( query, data )
    
    # class method to delete a user from the database
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db( query, data )

    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['fname']) < 3: #fname refers to the name attribute in the form in the html file, user is the dictionary we are passing in from server.py
            flash("First name must be at least 3 characters.")
            print("First name must be at least 3 characters.")
            is_valid = False
        if len(user['lname']) < 3:
            flash("Last name must be at least 3 characters.")
            print("Last name must be at least 3 characters.")
            is_valid = False
        if len(user['email']) < 3:
            flash("Email must be at least 3 characters.")
            print("Email must be at least 3 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Email must be in valid format.")
            print("Email must be in valid format.")
            is_valid = False
        #to ensure that the email is unique, we will query the database to see if the email already exists like so: query = "SELECT * FROM users WHERE email = %(email)s;" Do we need a different class method for this? No, we can use the get_one class method to do this like so: results = User.get_one(user) #user is the dictionary we are passing in from server.py
        #if the query returns a result, then we know that the email already exists in the database and we can flash a message to the user like so: flash("Email already exists.")
        #if the query does not return a result, then we know that the email does not exist in the database and we can proceed with the rest of our validation
        #so first we will start on line 77 with the query to check if the email already exists in the database and then we will continue with the rest of the validation
        return is_valid