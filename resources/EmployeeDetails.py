import sqlite3
import json
from pydantic import BaseModel

class EmployeeModel(BaseModel):
    Employee_ID: str
    Role: str | None = None
    Name: str | None = None
    Surname: str | None = None
    DateOfBirth: str | None = None

class EmployeeDetails_SRV:    
    DB_path ='./data/BookStore_DB.db'

    def createEmployee(self,employeeDetails):
        try:
            connection = sqlite3.connect(self.DB_path)            
            cursor = connection.cursor()
            keys = ['Employee_ID', 'Role','Name','Surname','DateOfBirth']
            values = list( map(employeeDetails.get, keys) )
            cursor.execute("INSERT INTO EmployeeTable Values(?,?,?,?,?)", values)
            connection.commit()
            output={"message":'Record Created'}
        except sqlite3.IntegrityError as e:
            output={"message":str(e) }
        finally:
            connection.close()        
            return output 
        
    
    def readAllEmployees(self):
        employeelist ={}
        try:
            connection = sqlite3.connect(self.DB_path)
            connection.row_factory = sqlite3.Row 
            cursor = connection.cursor()
            sql = "SELECT * FROM EmployeeTable"
            cursor.execute(sql)
            output = cursor.fetchall()            
        except:
            output={"message":'DB Connection Failed'}
        finally:
            connection.close()        
            return output

    def getEmployees(self,employeeDetails):
        where_i : str
        try:
            if employeeDetails['Employee_ID']:
                where_i = f"Employee_ID = '{employeeDetails['Employee_ID']}'"
            elif employeeDetails['Name']:
                where_i = f"Name = '{employeeDetails['Name']}'"
            elif employeeDetails['Surname']:
                where_i = f"Surname = '{employeeDetails['Surname']}'"           
            if where_i:    
                connection = sqlite3.connect(self.DB_path)
                connection.row_factory = sqlite3.Row 
                cursor = connection.cursor()
                sql = f"SELECT * FROM EmployeeTable where {where_i}"
                try:
                    cursor.execute(sql)                    
                    output = cursor.fetchone()
                    if output:
                        pass
                    else:
                        output = {"message":'Employee Does Not Exist'} 
                except:
                    output={"message":'DB Connection Failed'}
                finally:
                    connection.close() 
            else:
                output = {"message":'Please Search by Employee ID, Name or Surname'}  
        except:
            output = {"message":'Employee Not Found'}    
        finally:              
            return output   
    
    def updateEmployee(self,employeeDetails):
        try:
            if not employeeDetails["Employee_ID"]:
                output = {"message":"Please Use Employee ID to make Updates"}
            else:
                employeeDetails["Employee_ID"]
                connection = sqlite3.connect(self.DB_path)
                connection.row_factory = sqlite3.Row 
                cursor = connection.cursor()
                sql = f"""UPDATE EmployeeTable 
                            SET Role ='{employeeDetails['Role']}',
                            Name  ='{employeeDetails['Name']}',
                            Surname ='{employeeDetails['Surname']}',
                            DateOfBirth ='{employeeDetails['DateOfBirth']}'
                            where Employee_ID ='{employeeDetails['Employee_ID']}'"""
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
            output = {"message":'Employee Not Found'}  
        finally:
            return output   
    
    def deleteEmployee(self,employeeDetails):
        try:
            if not employeeDetails["Employee_ID"]:
                output = {"message":"Please Use Employee ID to Delete Employee"}
            else:
                employeeDetails["Employee_ID"]
                connection = sqlite3.connect(self.DB_path)
                connection.row_factory = sqlite3.Row 
                cursor = connection.cursor()
                sql = f"Delete From EmployeeTable where Employee_ID ='{employeeDetails['Employee_ID']}'"
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
            output = {"message":'Employee Not Found'}  
        finally:
            return output  
