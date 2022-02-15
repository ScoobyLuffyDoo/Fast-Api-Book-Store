from typing  import Optional
from fastapi import FastAPI
import BookDetailsService as booksrv
import sqlite3
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse



bookService =booksrv.bookDetails_SRV()
bookService =booksrv.bookDetails_SRV()
app = FastAPI()

@app.get('/')
def root():
    return("This is the book store API Service")

@app.get('/books/allbooks')    
def get_booksList():
    dic={}
    book_Responce = bookService.readAllBookDetails()  
    json_compatible_item_data = jsonable_encoder(book_Responce)
    return JSONResponse(content=json_compatible_item_data) 
    
@app.get('/bookdetails')
async def get_BookRecord(books:booksrv.Bookinfo_Request):
    book_Responce =books.dict()
    return book_Responce

@app.post('/books/Create')
async def create_BookRecord(books:booksrv.Bookinfo_Request):
    book_Responce =bookService.createBookDetails(books.dict())
    return book_Responce
# class user_dataBaseModel(BaseModel):
#     username: str = ""
#     id: str = ""
#     email: str = ""
#     firstName: str = ""
#     lastName:str = ""
#     createdTimestamp :int =0


# @app.put('/user',response_model=user_dataBaseModel)
# async def update_user(user_data: user_dataBaseModel):
#     update_item_encoded = jsonable_encoder(user_data)
#     print(update_item_encoded)
#     user_id = user_data.username
#     print(user_id)
#     return {"message": "DONE"}


# import sys         
  
# appending the directory of mod.py 
# in the sys.path list
# sys.path.append('D:/projects/base/app/modules')  
# uvicorn index:app --reload



# @app.get('/booksdetailsXD')
# def get_book(book_id:Optional[int] = None,name: Optional[str]=None,author:Optional[str]=None):
#     if book_id == None:
#        print("Search By Author")      
#     book_Responce = bookService.readBookDetails()            
#     return{"BookInfo":book_Responce}
    # return{"BookInfo":{"book_id":book_id, "name":name, "author":author}}