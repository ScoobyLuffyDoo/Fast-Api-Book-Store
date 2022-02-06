import sqlite3 
# DB : BookStore_DB
# TB : BooksTable
# TB : EmployeeTable
# TB : UserTable

connection = sqlite3.connect("BookStore_DB.db")

# Create Book Store Data Base
cursor = connection.cursor()




#---------------------------#
# Create Book Details Table #
#---------------------------#
bookDetailsTable_CMD = """CREATE TABLE IF NOT EXISTS
BooksTable(
    Book_ID INTEGER PRIMARY KEY,
    name TEXT,
    author TEXT,
    checkout_Status INTEGER,
    last_checkout_date TEXT,
    return_date TEXT
)
"""
# execute Create table
cursor.execute(bookDetailsTable_CMD)
#============================================================================


#-----------------------#
# Create employee Table #
#-----------------------#
employeeTable_CMD = """CREATE TABLE IF NOT EXISTS
EmployeeTable(
    employee_ID INTEGER PRIMARY KEY,
    role TEXT,
    name TEXT,
    surname TEXT,
    date_of_birth TEXT
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
    user_ID INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    date_of_birth TEXT
)
"""
# execute Create table
cursor.execute(userDetailsTable_CMD)
#============================================================================


connection.close()