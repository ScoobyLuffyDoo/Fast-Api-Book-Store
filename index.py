from typing  import Optional
from fastapi import FastAPI
import BookDetailsService as booksrv




app = FastAPI()

@app.get('/')
def root():
    return("This is the book store API Service")

@app.get('/books/bookregister')    
def get_booksList():
    return("This will get all the books in Json format")

@app.get('/books/bookinfo')    
def get_book(book_id:Optional[int] = None,name: Optional[str]=None,author:Optional[str]=None):
    if book_id == None:
       print("Search By Author")    
    return{"BookInfo":{"book_id":book_id, "name":name, "author":author}}
    
@app.post('/books/Create')
async def create_BookRecord(books:booksrv.Bookinfo_Request):
    return{"BookData":books}

@app.get('/booksdetails') 
def get_bookDetails():

    return(output)



# uvicorn index:app --reload