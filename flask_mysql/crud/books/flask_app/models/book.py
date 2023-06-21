from flask_app.config.mysqlconnection import connectToMySQL #this is connecting to the database
from flask_app.models import author #this is importing the author model FILE and not the class so we can use it in the book class methods (like "author.Author(data)"), thru circular importing (refer to line 2 and 46)

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # list of the authors who has favorited this book,  this will be populated in the get_by_id method and used in the show_book.html file
        self.authors_who_favorited = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        books = []
        results = connectToMySQL('books_schema').query_db(query)
        for row in results: #type: ignore
            books.append(cls(row))
        return books
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO books (title,num_of_pages) VALUES (%(title)s,%(num_of_pages)s);"
        return connectToMySQL('books_schema').query_db(query,data)

#this method grabs a book by its id and adds all the authors who favorited it to the book object to be used in the show_book.html file
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)

        book = cls(results[0])  #type: ignore

        for row in results: #type: ignore
            if row['authors.id'] == None:
                break
            data = {
                "id": row['authors.id'],
                "name": row['name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.authors_who_favorited.append(author.Author(data)) #we are using circular imports here, so we need to import the author model in this file. If not we will get an error. The ciricular import is in the ""
        return book

    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
        results = connectToMySQL('books_schema').query_db(query,data)
        books = []
        for row in results: #type: ignore
            books.append(cls(row))
        print(books)
        return books