import sqlite3
import json
from pydantic import BaseModel

class UserInfo_Request(BaseModel):
    User_ID: str
    Name: str
    Surname: str
    DateOfBirth: str

class UserDetails_SRV:    
     DB_path ='./data/BookStore_DB.db'