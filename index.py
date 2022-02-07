from typing  import Optional
from fastapi import FastAPI
import sqlite3
path='BookStore_DB.db'



app = FastAPI()

@app.get('/')
def Blha():
    return("Welcome to the Book Store")

@app.get('/booksdetails') 
def get_bookDetails():
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    sql = "SELECT * FROM BooksTable"
    cursor.execute(sql)
    output = cursor.fetchmany(5)
    connection.close()
    return(output)

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    print(type(fake_items_db))
    return fake_items_db[skip : skip + limit]