from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja #importing the function that will return an instance of a connection

class Dojo:
    DB = 'dojos_and_ninjas_schema'
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = [] # we will fill this up later

    # Now we use class methods to query our database
    # class methods to get all dojos from the database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results: # type: ignore
            dojos.append( cls(dojo) )
        return dojos
    
    # class method to get a dojo from the database
    @classmethod
    def get_one(cls, data ): #here we use left join to get all the ninjas associated with a dojo by joining the dojo_id from the ninjas table with the id from the dojos table
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;" #%(id)s is a placeholder for the id we will get from the data dictionary we pass into the method from dojos controller
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls( results[0] ) # type: ignore
    
    # class method to add/save a dojo to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"
        return connectToMySQL(cls.DB).query_db( query, data ) 

    
    #in this method we are deleting a dojo and all the ninjas associated with it    
    @classmethod
    def delete(cls, data ): 
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db( query, data ) 
    
    # class method to get all ninjas from the database
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        dojo = cls(results[0]) # type: ignore
        for db_row in results: # type: ignore
            ninja_data = {
                "id": db_row["ninjas.id"],
                "first_name": db_row["first_name"],
                "last_name": db_row["last_name"],
                "age": db_row["age"],
                "created_at": db_row["ninjas.created_at"],
                "updated_at": db_row["ninjas.updated_at"],
                "dojo_id": db_row["dojo_id"]
            }
            dojo.ninjas.append(Ninja(ninja_data))
        print(dojo.ninjas)
        return dojo
