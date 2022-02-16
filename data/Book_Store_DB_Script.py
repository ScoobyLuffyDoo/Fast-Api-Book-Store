import sqlite3 
# DB : BookStore_DB
# TB : BooksTable
# TB : EmployeeTable
# TB : UserTable
# TB : BookRegistryRegistryTable

connection = sqlite3.connect("BookStore_DB.db")

# Create Book Store Data Base
cursor = connection.cursor()

#---------------------------#
# Create Book Details Table #
#---------------------------#
bookDetailsTable_CMD = """CREATE TABLE IF NOT EXISTS
BooksTable(
    Book_ID TEXT PRIMARY KEY,
    Name TEXT,
    Author TEXT,
    CaptureDate TEXT
)
"""
# execute Create table
cursor.execute(bookDetailsTable_CMD)
#============================================================================


#---------------------------#
# Create Employee Table     #
#---------------------------#
employeeTable_CMD = """CREATE TABLE IF NOT EXISTS
EmployeeTable(
    Employee_ID TEXT PRIMARY KEY,
    Role TEXT,
    Name TEXT,
    Surname TEXT,
    DateOfBirth TEXT
)
"""
# execute Create table
cursor.execute(employeeTable_CMD)
#============================================================================

#---------------------------#
# Create User Details Table #
#---------------------------#
userDetailsTable_CMD = """CREATE TABLE IF NOT EXISTS
UserTable(
    User_ID TEXT PRIMARY KEY,
    Name TEXT,
    Surname TEXT,
    DateOfBirth TEXT
)
"""
# execute Create table
cursor.execute(userDetailsTable_CMD)
#============================================================================

#---------------------------#
# Create Registry Table     #
#---------------------------#
registryDetailsTable_CMD = """CREATE TABLE IF NOT EXISTS
BookRegistryRegistryTable(
    CheckOut_ID INTEGER PRIMARY KEY,
    Book_ID TEXT,
    User_ID TEXT,
    Employee TEXT,
    Status INTEGER,
    CheckOutDate TEXT,
    ReturnDate TEXT
)
"""
# execute Create table
cursor.execute(registryDetailsTable_CMD)
#============================================================================


connection.close()