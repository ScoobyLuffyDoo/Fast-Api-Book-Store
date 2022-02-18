from typing  import Optional
from fastapi import FastAPI
import resources
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


bookService = resources.BookDetails_SRV()
app = FastAPI()

# Root Path
@app.get('/')
def root():
    return("This is the book store API Service")

# Get All Book Details
@app.get('/bookdetails/allbooks')    
def get_booksList():
    book_Response = bookService.readAllBookDetails()  
    json_compatible_item_data = jsonable_encoder(book_Response)
    return JSONResponse(content=json_compatible_item_data)

# Get Single Book Revord
@app.get('/bookdetails')
async def get_BookRecord(books:resources.BookInfo_Request):
    book_Response =books.dict()
    response = bookService.getBookDetail(book_Response)
    return response

# Create Book Record
@app.post('/bookdetails/Create')
async def create_BookRecord(books:resources.BookInfo_Request):
    book_Response =bookService.createBookDetails(books.dict())
    return response
    
# Update Book Details
@app.put('/bookdetials/update')
async def delete_BookRecord(books):
    return{books}

@app.get('/user/all_users')    
def get_booksList():
    book_Response = bookService.readAllBookDetails()  
    json_compatible_item_data = jsonable_encoder(book_Response)
    return JSONResponse(content=json_compatible_item_data)

@app.get('/userdetails')
async def get_BookRecord(books:resources.BookInfo_Request):
    book_Response =books.dict()
    return book_Response

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
#     book_Response = bookService.readBookDetails()            
#     return{"BookInfo":book_Response}
    # return{"BookInfo":{"book_id":book_id, "name":name, "author":author}}