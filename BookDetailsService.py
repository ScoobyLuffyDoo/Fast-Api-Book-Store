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
        bookslist ={}
        # try:
        connection = sqlite3.connect(self.DB_path)
        connection.row_factory = sqlite3.Row 
        cursor = connection.cursor()
        sql = "SELECT * FROM BooksTable"
        cursor.execute(sql)
        output = cursor.fetchall()
        # output =json.dumps(output)
        # output =json.dumps( [dict(ix) for ix in sql] )
        connection.close()        

        return output

        # except:
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

