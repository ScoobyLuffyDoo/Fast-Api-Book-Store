from typing import Optional
import sqlite3
import json
from pydantic import BaseModel

class BookInfo_Request(BaseModel):
    Book_ID: str
    Name: Optional[str] = None
    Author: Optional[str] = None
    CaptureDate: Optional[str] = None

class BookDetails_SRV:    
    DB_path ='./data/BookStore_DB.db'   

    # Create Book Details Function
    def createBookDetails(self,bookDetails):
        try:
            connection = sqlite3.connect(self.DB_path)            
            cursor = connection.cursor()
            keys = ['Book_ID', 'Name','Author','CaptureDate']
            values = list( map(bookDetails.get, keys) )
            cursor.execute("insert into BooksTable Values(?,?,?,?)", values)
            connection.commit()
            output={"message":'Record Created'}
        except sqlite3.IntegrityError as e:
            output={"message":str(e) }
        finally:
            connection.close()        
            return output 

    # Get All BookDetails 
    def readAllBookDetails(self):
        bookslist ={}
        try:
            connection = sqlite3.connect(self.DB_path)
            connection.row_factory = sqlite3.Row 
            cursor = connection.cursor()
            sql = "SELECT * FROM BooksTable"
            cursor.execute(sql)
            output = cursor.fetchall()            
        except:
            output={"message":'DB Connection Failed'}
        finally:
            connection.close()        
            return output
            
    # Get Single Book Details
    def getBookDetail(self,bookDetails):
        bookslist = {}
        where_i : str
        try:
            if bookDetails['Book_ID']:
                where_i = f"Book_ID = '{bookDetails['Book_ID']}'"
            elif bookDetails['Author']:
                where_i = f"Author = '{bookDetails['Author']}'"
            elif bookDetails['Name']:
                where_i = f"Name = '{bookDetails['Name']}'"           
            if where_i:    
                connection = sqlite3.connect(self.DB_path)
                connection.row_factory = sqlite3.Row 
                cursor = connection.cursor()
                sql = f"SELECT * FROM BooksTable where {where_i}"
                try:
                    cursor.execute(sql)                    
                    output = cursor.fetchone()
                    if output:
                        pass
                    else:
                        output = {"message":'Book Does Not Exist'} 
                except:
                    output={"message":'DB Connection Failed'}
                finally:
                    connection.close() 
            else:
                output = {"message":'Please Search by Book ID, Name or Author'}  
        except:
            output = {"message":'Book Not Found'}    
        finally:              
            return output      

    def updateBookDetails(self,bookDetails):
        try:
            if not bookDetails["Book_ID"]:
                output = {"message":"Please Use Book ID to make Updates"}
            else:
                bookDetails["Book_ID"]
                connection = sqlite3.connect(self.DB_path)
                connection.row_factory = sqlite3.Row 
                cursor = connection.cursor()
                sql = f"""UPDATE BooksTable 
                            SET Name ='{bookDetails['Name']}',
                            Author  ='{bookDetails['Author']}',
                            CaptureDate ='{bookDetails['CaptureDate']}'
                            where Book_ID ='{bookDetails['Book_ID']}'"""
                print(sql)
                try:
                    cursor.execute(sql)
                    connection.commit()                        
                    output = {"message":"Update Complete"}
                except:
                    output={"message":'DB Connection Failed'}
                finally:
                    connection.close()                 
        except:
            output = {"message":'Book Not Found'}  
        finally:
            return output    
    def deleteBookDetails(self,bookDetails):
        try:
            if not bookDetails["Book_ID"]:
                output = {"message":"Please Use Book ID to make Updates"}
            else:
                bookDetails["Book_ID"]
                connection = sqlite3.connect(self.DB_path)
                connection.row_factory = sqlite3.Row 
                cursor = connection.cursor()
                sql = f"Delete From BooksTable where Book_ID ='{bookDetails['Book_ID']}'"
                print(sql)
                try:
                    cursor.execute(sql)
                    connection.commit()                        
                    output = {"message":"Delete Complete"}
                except:
                    output={"message":'DB Connection Failed'}
                finally:
                    connection.close()                 
        except:
            output = {"message":'Book Not Found'}  
        finally:
            return output  
