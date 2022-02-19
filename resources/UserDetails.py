import sqlite3
import json
from pydantic import BaseModel

class UserModel(BaseModel):
    User_ID: str
    Name: str | None = None
    Surname: str | None = None
    DateOfBirth: str | None = None

class UserDetails_SRV:    
    DB_path ='./data/BookStore_DB.db'

    def createUser(self,userDetails):
        try:
            connection = sqlite3.connect(self.DB_path)            
            cursor = connection.cursor()
            keys = ['User_ID', 'Name','Surname','DateOfBirth']
            values = list( map(userDetails.get, keys) )
            cursor.execute("INSERT INTO UserTable Values(?,?,?,?)", values)
            connection.commit()
            output={"message":'Record Created'}
        except sqlite3.IntegrityError as e:
            output={"message":str(e) }
        finally:
            connection.close()        
            return output 

    def readAllUsers(self): 
        employeelist ={}
        try:
            connection = sqlite3.connect(self.DB_path)
            connection.row_factory = sqlite3.Row 
            cursor = connection.cursor()
            sql = "SELECT * FROM UserTable"
            cursor.execute(sql)
            output = cursor.fetchall()            
        except:
            output={"message":'DB Connection Failed'}
        finally:
            connection.close()        
            return output

    def getUser(self,userDetails): 
        where_i : str
        try:
            if userDetails['User_ID']:
                where_i = f"User_ID = '{userDetails['User_ID']}'"
            elif userDetails['Name']:
                where_i = f"Name = '{userDetails['Name']}'"
            elif userDetails['Surname']:
                where_i = f"Surname = '{userDetails['Surname']}'"           
            if where_i:    
                connection = sqlite3.connect(self.DB_path)
                connection.row_factory = sqlite3.Row 
                cursor = connection.cursor()
                sql = f"SELECT * FROM UserTable where {where_i}"
                try:
                    cursor.execute(sql)                    
                    output = cursor.fetchone()
                    if output:
                        pass
                    else:
                        output = {"message":'User Does Not Exist'} 
                except:
                    output={"message":'DB Connection Failed'}
                finally:
                    connection.close() 
            else:
                output = {"message":'Please Search by User ID, Name or Surname'}  
        except:
            output = {"message":'Employee Not Found'}    
        finally:              
            return output   
    
    def updateUser(self,userDetails):
        try:
            if not userDetails["User_ID"]:
                output = {"message":"Please Use Employee ID to make Updates"}
            else:
                userDetails["User_ID"]
                connection = sqlite3.connect(self.DB_path)
                connection.row_factory = sqlite3.Row 
                cursor = connection.cursor()
                sql = f"""UPDATE UserTable 
                            SET Name  ='{userDetails['Name']}',
                            Surname ='{userDetails['Surname']}',
                            DateOfBirth ='{userDetails['DateOfBirth']}'
                            where User_ID ='{userDetails['User_ID']}'"""
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
            output = {"message":'User Not Found'}  
        finally:
            return output   
    
    def deleteUser(self,userDetails):
        try:
            if not userDetails["User_ID"]:
                output = {"message":"Please Use Employee ID to Delete Employee"}
            else:
                userDetails["User_ID"]
                connection = sqlite3.connect(self.DB_path)
                connection.row_factory = sqlite3.Row 
                cursor = connection.cursor()
                sql = f"Delete From UserTable where User_ID ='{userDetails['User_ID']}'"
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
            output = {"message":'User Not Found'}  
        finally:
            return output 