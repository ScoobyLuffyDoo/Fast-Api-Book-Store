import sqlite3
import json
# https://fastapi.tiangolo.com/tutorial/body/


class bookDetails_SRV:    
    def createBookDetails(self,bookDetials):
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