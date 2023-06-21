from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #this is for flash messages # type: ignore

class Burger: 
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# gets all the burgers and returns them in a list of burger objects .
    @classmethod
    def save(cls,data):
        query = "INSERT INTO burgers (name,bun,meat,calories,created_at,updated_at) VALUES (%(name)s,%(bun)s,%(meat)s,%(calories)s,NOW(),NOW())"
        return connectToMySQL('burgerz').query_db(query,data) #the 'burgers' is the name of the database in mysql

# gets all the burgers and returns them in a list of burger objects .
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers;"
        burgers_from_db =  connectToMySQL('burgerz').query_db(query)
        burgers =[]
        for b in burgers_from_db: # type: ignore
            burgers.append(cls(b))
        return burgers

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM burgers WHERE burgers.id = %(id)s;"
        burger_from_db = connectToMySQL('burgerz').query_db(query,data)

        return cls(burger_from_db[0]) # type: ignore

    @classmethod
    def update(cls,data):
        query = "UPDATE burgers SET name=%(name)s, bun=%(bun)s, meat=%(meat)s, calories=%(calories)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('burgerz').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM burgers WHERE id = %(id)s;"
        return connectToMySQL('burgerz').query_db(query,data)
    

    # Other Burger methods remain up yonder.
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    @staticmethod
    def validate_burger(burger): # burger is a dictionary in the form of request.form but doesnt exist yet until we create it in server.py
        is_valid = True # we assume this is true
        if len(burger['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(burger['bun']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        if len(burger['meat']) < 3:
            flash("Meat must be at least 3 characters.")
            is_valid = False
        if int(burger['calories']) < 200:
            flash("Calories must be 200 or greater.")
            is_valid = False
        return is_valid # if is_valid is False, the form didn't validate
