from mysqlconnection import connectToMySQL
# model the class after the user table from our database
class User:
    def __init__(self , data):#data is a dictionary#we want to ensure the keys in the dictionary match the fields in the table#we could iterate through the data dictionary and set the keys as attributes, but we want to ensure we have the keys in our dictionary as attributes
        self.id = data['id']#data should be a dictionary with all the data from a row in the database
        self.first_name = data['first_name']#we could loop through the data dictionary and set the keys as attributes, but we want to ensure we have the keys in our dictionary as attributes
        self.last_name = data['last_name']#loop through the data dictionary and set the keys as attributes with the value of the key as the value of the attribute
        self.email = data['email']#
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):#cls is the class that is calling the method
        query = "SELECT * FROM users;"
        results= connectToMySQL('users_schema').query_db(query)#run the query
        users = []#create an empty list to append our instances of users
        for user in results:#iterate through the db results and create instances of users with cls
            users.append(cls(user))#append the user to the list
        return users#return the list of users
    # class method to save our user to the database
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"#define the query
        result = connectToMySQL('users_schema').query_db(query,data)#run the query
        return result#return the id of the inserted row
    # class method to get a user from the database using the id
    @classmethod
    def get_one(cls,id):
        query = "SELECT * FROM users WHERE id = %(id)s;"#define the query
        result = connectToMySQL('users_schema').query_db(query,{'id':id})#run the query
        return cls(result[0])#return the user object
    # class method to update a user in the database
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        print("Update Method - Data:", data)  # Print the data dictionary for debugging purposes
        result = connectToMySQL('users_schema').query_db(query, data)
        return result

    # class method to delete a user from the database
    @classmethod
    def delete(cls,id):#cls is the class that is calling the method
        query = "DELETE FROM users WHERE id = %(id)s;"#define the query
        result = connectToMySQL('users_schema').query_db(query,{'id':id})#run the query
        return result#return the id of the inserted row
    
    