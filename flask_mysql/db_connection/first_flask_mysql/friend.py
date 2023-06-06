#We are using OOP to create a class, modeled after our MySQL ERD table: friends , that will handle all of our database queries.

# import the function that will return an instance of a connection, this is needed to connect to the database and run queries
from mysqlconnection import connectToMySQL

# model the class after the friends table from our database
class Friend:
    DB="first_flask" #this is the name of the database (schema) we are connecting to, you could change this to a different database that you have created
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name'] #data is a dictionary that contains all of the data from a row in the database, so you can access the data with the keys from the table as the keys in the dictionary
        self.last_name = data['last_name'] 
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    #class methods to get all friends from the database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting. We need to call on the connectToMySQL function every time we want to execute a query because our connection closes as soon as the query finishes executing.
        results = connectToMySQL(cls.DB).query_db(query) #the .query_db() method returns a list of dictionaries, in this case, a list of dictionaries of the friends table from the database. It takes in the argument of the query we want to run.
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls (the class that this method is inside of, which is Friend). The db results are dictionaries.
        for friend in results: # type: ignore
            friends.append( cls(friend) )
        return friends

#class method to get one friend from the database
    @classmethod
    def get_one(cls, friend_id):
        query  = "SELECT * FROM friends WHERE id = %(id)s;"
        data = {'id': friend_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0]) # type: ignore

    #class method to add/save a friend to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
        # one of the variables is called data, the other is called query. the variables in the query string need to match the keys in the data dictionary, for example, %(fname)s needs to match the key "fname" in the data dictionary.
        
        # data is a dictionary that will be passed into the save method from server.py. 
        # The keys in data need to exactly match the columns in the table. For example, the key "fname" in data needs to match the column "first_name" in the table.
        
        return connectToMySQL(cls.DB).query_db( query, data ) #the .query_db() method returns the id of the row that was created in the database. We will use this id to find the friend we just created in the database.


    @classmethod
    def update(cls, data ):
        query = "UPDATE friends SET first_name=%(fname)s, last_name=%(lname)s, occupation=%(occ)s, updated_at=NOW() WHERE id=%(id)s;"
        results= connectToMySQL(cls.DB).query_db( query, data ) 
        return results
#This method will update the friend in the database with the id that matches the id in the data dictionary. The data dictionary is passed in from server.py. The keys in the data dictionary need to match the columns in the table.
#the WHERE clause is very important. If we don't include it, then every row in the table will be updated. We only want to update the row that matches the id in the data dictionary.


# the delete method will be used when we need to delete a friend from our database
    @classmethod
    def delete(cls, friend_id):
        query  = "DELETE FROM friends WHERE id = %(id)s;" # %(id)s is the key in the data dictionary that will be passed into the delete method from server.py
        data = {"id": friend_id} # data is a dictionary that will be passed into the delete method from server.py
        return connectToMySQL(cls.DB).query_db(query, data)