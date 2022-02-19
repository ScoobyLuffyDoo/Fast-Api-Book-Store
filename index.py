from typing  import Optional
from fastapi import FastAPI
import resources
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json


bookService = resources.BookDetails_SRV()
EmployeeService = resources.EmployeeDetails_SRV()
app = FastAPI()

# Root Path
@app.get('/')
def root():
    return("This is the book store API Service")

# Get All Book Details
@app.get('/books/all')    
async def get_booksList():
    book_Response = bookService.readAllBookDetails()  
    json_compatible_item_data = jsonable_encoder(book_Response)
    return {"books":book_Response}
    
# Get Single Book Record
@app.get('/books')
async def get_Book(books:resources.BookInfoModel):
    response = bookService.getBookDetail(books.dict()) 
    return response

# Create Book Record
@app.post('/books/create')
async def create_BookRecord(books:resources.BookInfoModel):
    response =bookService.createBookDetails(books.dict())
    return response
    
# Update Book Details
@app.put('/books/update')
async def update_BookRecord(books:resources.BookInfoModel):
    bookItemsUpdate = jsonable_encoder(books.dict())
    response = bookService.updateBookDetails(bookItemsUpdate)
    return response

# Delete Book Details
@app.delete('/books/delete')
async def delete_BookRecord(books:resources.BookInfoModel):
    bookItemsDelete = jsonable_encoder(books.dict())
    response = bookService.deleteBookDetails(bookItemsDelete)
    return response

# ******************************
# *       Emplyee Details      *
# ******************************

# Get Single Employee Record
@app.get('/employee')
async def get_Employee(employee:resources.EmployeeModel):
    response = EmployeeService.getEmployees(employee.dict())
    return response
    
# Get All Employees Data
@app.get('/employee/all')    
async def get_EmployeeList():
    response = EmployeeService.readAllEmployees()
    return {"employees":response}

# Create Employees Record
@app.post('/employee/create')
async def create_EmployeeRecord(employee:resources.EmployeeModel): 
    response = EmployeeService.createEmployee(employee.dict()) 
    return response

# Update Book Details
@app.put('/employee/update')
async def update_EmployeeRecord(employee:resources.EmployeeModel): 
    employeeItemsUpdate = jsonable_encoder(employee.dict())
    response = EmployeeService.updateEmployee(employeeItemsUpdate) 
    return response

# Delete Book Details
@app.delete('/employee/delete')
async def delete_EmployeeRecord(employee:resources.EmployeeModel):
    employeeItemsDelete = jsonable_encoder(employee.dict())
    response = EmployeeService.deleteEmployee(employeeItemsDelete)
    return response



if __name__ =="__main__":
     main()    

# uvicorn index:app --reload

