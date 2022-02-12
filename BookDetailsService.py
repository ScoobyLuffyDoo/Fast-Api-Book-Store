import sqlite3
import json
from pydantic import BaseModel

class Bookinfo_Request(BaseModel):
    Book_ID: str
    Name: str
    Author: str
    CaptureDate: int

class bookDetails_SRV:    
    DB_path ='./BookStoreData/BookStore_DB.db'
    def createBookDetails(self,bookDetails):
        return{"message":'Busy'}
    def readBookDetails(self):
        try:
            connection = sqlite3.connect(self.DB_path)
            cursor = connection.cursor()
            sql = "SELECT * FROM BooksTable"
            cursor.execute(sql)
            output = cursor.fetchall()
            print(type(output))
            for books in output:
                print(books)
            connection.close()            
            return output
        except:
            return{'Error':"Connection to DB Failed"}
    def updateBookDetails(self):
        return tst    
    def deleteBookDetails(self):
        return tst
    def jsonResponseBookDetails(self,bookDetails):
        json_build=()
        for books in bookDetails:
            json_build
        return BookDetails_Json


# Book Body
# {
#     "name": "Foo",
#     "description": "An optional description",
#     "price": 45.2,
#     "tax": 3.5 
# }

