from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash #type: ignore
from flask_app import app 
from flask_app.models import user

DB = 'recipe_schema'
class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['users_id'] 
        self.user = []

    @classmethod
    def save_recipe(cls,data):
        query = "INSERT INTO recipes (name, description, instructions, date_cooked, under_30, users_id, created_at, updated_at) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_30)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL(DB).query_db(query,data)
    
    
    @classmethod
    def get_all_recipes_with_chef(cls): 
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.users_id;"
        results = connectToMySQL(DB).query_db(query)
        recipes = []
        for recipe in results: #type: ignore
            one_recipe = cls(recipe)
            chef_data = {
                "id": recipe['users.id'],
                "first_name": recipe['first_name'],
                "last_name": recipe['last_name'],
                "email": recipe['email'],
                "password": recipe['password'],
                "created_at": recipe['users.created_at'],
                "updated_at": recipe['users.updated_at']
            }
            one_recipe.user = user.User(chef_data)
            recipes.append(one_recipe)
        return recipes
    
    @classmethod
    def update_recipe(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_cooked = %(date_cooked)s, under_30 = %(under_30)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def delete_recipe(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod 
    def get_recipes_by_id(cls,data): #this method will get a specific recipe by its id
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.users_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        recipe= cls(results[0]) #type: ignore
        chef_data = {
            "id": results[0]['users.id'], #type: ignore
            "first_name": results[0]['first_name'], #type: ignore
            "last_name": results[0]['last_name'], #type: ignore 
            "email": results[0]['email'], #type: ignore
            "password": results[0]['password'], #type: ignore
            "created_at": results[0]['users.created_at'], #type: ignore
            "updated_at": results[0]['users.updated_at']  #type: ignore
        }   
        recipe.user = user.User(chef_data)
        return recipe
    

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 1: 
            flash("Recipe name cannot be blank.", 'recipe') 
            is_valid = False
        if len(data['description']) < 1:
            flash("Recipe description cannot be blank.", 'recipe')
            is_valid = False
        if len(data['instructions']) < 1:
            flash("Recipe instructions cannot be blank.", 'recipe')
            is_valid = False
        if not data['under_30']: 
            flash("Please select whether your recipe is under 30 minutes or not.", 'recipe')
            is_valid = False
        if len(data['date_cooked']) < 1:
            flash("Please select a date.", 'recipe')
            is_valid = False
        return is_valid
