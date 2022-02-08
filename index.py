from typing  import Optional
from fastapi import FastAPI

path='BookStore_DB.db'



app = FastAPI()

@app.get('/')
def Blha():
    return("Welcome to the Book Store")

@app.get('/booksdetails') 
def get_bookDetails():

    return(output)

@app.post('/bookdetail/bookinfo')
def create_BookRecord(TST:bookinfo):
    print(TST)

# uvicorn index:app --reload