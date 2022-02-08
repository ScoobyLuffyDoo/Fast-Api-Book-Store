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
    def createBookDetails(self,bookDetails):
        return tst
    def readBookDetails(self):
        return tst
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


# connection = sqlite3.connect(path)
#     cursor = connection.cursor()
#     sql = "SELECT * FROM BooksTable"
#     cursor.execute(sql)
#     output = cursor.fetchmany(5)
#     connection.close()
#     tst =json.dumps(output)
#     print(output)