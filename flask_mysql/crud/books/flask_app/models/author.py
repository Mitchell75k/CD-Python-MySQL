from flask_app.config.mysqlconnection import connectToMySQL #this is connecting to the database
from flask_app.models import book #this is importing the book model FILE and not the class so we can use it in the author class methods (like "book.Book(data)"), thru circular importing (refer to line 2 and 66)

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.favorite_books = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        authors = []
        results = connectToMySQL('books_schema').query_db(query)
        for row in results: #type: ignore
            authors.append(cls(row))
        return authors

    @classmethod
    def save(cls,data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        return connectToMySQL('books_schema').query_db(query,data)

    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );" #here we are selecting all authors that are not in the favorites table for the book we are looking at 
        authors = []
        results = connectToMySQL('books_schema').query_db(query,data)
        for row in results: #type: ignore
            authors.append(cls(row))
        return authors


#this method adds a favorite to the favorites table
    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books_schema').query_db(query,data); 


#this method gets all the favorites for a specific author and adds them to the author object to be used in the show_author.html file 
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)

        # Creates instance of author object from row one
        author = cls(results[0]) #type: ignore
        # append all book objects to the instances favorites list.               
        for row in results: #type: ignore
            # if there are no favorites
            if row['books.id'] == None:
                break
            # common column names come back with specific tables attached
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.favorite_books.append(book.Book(data)) #we are using circular import here to create a new book object and add it to the author's favorite books list because we imported the book class at the top of this file
        return author
    #we are adding the book to the favorites table and then we are getting the author by id and adding the book to the author's favorite books list