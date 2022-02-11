import sqlite3
import json
from pydantic import BaseModel

class Bookinfo_Request(BaseModel):
    Book_ID: int
    Name: str
    Author: str
    CheckoutStatus: int
    LastCheckoutDate: str
    LastReturnDate:str

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
            output = cursor.fetchmany(5)
            connection.close()
            return output
        except:
            return{'Error':"Connection to DB Failed"}
    def updateBookDetails(self):
        return tst    
    def deleteBookDetails(self):
        return tst


# Book Body
# {
#     "name": "Foo",
#     "description": "An optional description",
#     "price": 45.2,
#     "tax": 3.5 
# }

