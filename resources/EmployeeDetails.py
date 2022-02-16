import sqlite3
import json
from pydantic import BaseModel

class Employee_Request(BaseModel):
    Employee_ID: str
    Role: str
    Name: str
    Surname: str
    DateOfBirth: str

class EmployeeDetails_SRV:    
     DB_path ='./data/BookStore_DB.db'