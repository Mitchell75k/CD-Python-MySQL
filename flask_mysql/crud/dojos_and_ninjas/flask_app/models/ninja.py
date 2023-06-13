from flask_app.config.mysqlconnection import connectToMySQL #importing the function that will return an instance of a connection

class Ninja:
    DB = 'dojos_and_ninjas_schema'
    def __init__( self , data ):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name  = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = data['dojo_id'] # we will fill this up later, this will be used for the foreign key relationship


    # Now we use class methods to query our database

    # class methods to get all ninjas from the database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.DB).query_db(query)
        ninjas = []
        for ninja in results: # type: ignore
            ninjas.append( cls(ninja) )
        return ninjas
    
    # class method to get a ninja from the database
    @classmethod
    def get_one(cls, data ):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls( results[0] ) # type: ignore
    
    # class method to add/save a ninja to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( dojo_id, first_name, last_name, age, created_at, updated_at ) VALUES ( %(dojo_id)s, %(fname)s, %(lname)s, %(age)s, NOW() , NOW() );"
        return connectToMySQL(cls.DB).query_db( query, data )
    
    # class method to delete a ninja from the database
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db( query, data )