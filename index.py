from typing  import Optional
from fastapi import FastAPI
from pydantic import BaseModel

path='BookStore_DB.db'

class Bookinfo(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get('/')
def Blha():
    return("Welcome to the Book Store")

@app.post('/books/Create')
async def create_BookRecord(books:Bookinfo):
    return{"BookData":books}

@app.get('/booksdetails') 
def get_bookDetails():

    return(output)



# uvicorn index:app --reload