from flask_app.config.mysqlconnection import connectToMySQL #importing the function that will return an instance of a connection

class Ninja:
    DB = 'dojos_and_ninjas_schema'
    def __init__( self , data ):
        self.id = data['id']
        self.dojo_id = data['dojo_id'] # this is the id of the dojo the ninja belongs to, this comes from the foreign key in the ninjas table
        self.first_name = data['first_name']
        self.last_name  = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Now we use class methods to query our database

    # class methods to get all ninjas from the database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.DB).query_db(query)
        ninjas = []
        for ninja in results: # type: ignore #here we are looping through the results and appending each row to the ninjas list
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
        query = "INSERT INTO ninjas ( first_name, last_name, age, dojo_id, created_at, updated_at ) VALUES ( %(fname)s, %(lname)s, %(age)s, %(dojo_id)s, NOW() , NOW() );"
        return connectToMySQL(cls.DB).query_db( query, data )
    
    # class method to delete a ninja from the database
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db( query, data )
    
    # class method to update a ninja in the database
    @classmethod
    def update(cls, data ):
        query = "UPDATE ninjas SET first_name = %(fname)s, last_name = %(lname)s, age = %(age)s, dojo_id = %(dojo_id)s, updated_at = NOW() WHERE id = %(id)s;" # remember that the %(fname)s, %(lname)s, %(age)s, %(dojo_id)s are referring to the keys in the data dictionary
        return connectToMySQL(cls.DB).query_db( query, data )