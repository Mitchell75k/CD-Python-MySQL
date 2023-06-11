from mysqlconnection import connectToMySQL
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
