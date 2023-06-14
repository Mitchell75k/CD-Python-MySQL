# a cursor is the object we use to interact with the database
import pymysql.cursors               

# this class gives us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'me020402',  
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = False)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query:str, data:dict=None): # data is optional because not all queries will need them. This method will be used to run SELECT, INSERT, UPDATE, and DELETE queries on the database from our python files. # type: ignore
        with self.connection.cursor() as cursor:
            try: #here we are trying to run the query with the data
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                cursor.execute(query)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
# Now we can use this function in our user.py file to connect to our database!
