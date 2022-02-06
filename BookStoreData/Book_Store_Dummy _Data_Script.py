import sqlite3

connection = sqlite3.connect("BookStore_DB.db")

cursor = connection.cursor()

#-------------------------------------------------------------------#
#                Create Book Details Data                           #
# BooksTable                                                        #
# Book_ID, Name, Author, CheckoutStatus, CheckoutDate, ReturnDate   #
#-------------------------------------------------------------------#
BookDetailsData =[
    (1,"Scooby Doo and the Pirate Treasure","James Gelsey",1,"2022-01-23","2022,02,06"),
    (2,"Rats of NIMH","Robert C. O'Brien",0,"",""),
    (3,"The Chronicles of Narnia","C. S. Lewis",1,"2022-01-25","2022,02,16"),
    (4,"Percy Jackson & the Olympians","Rick Riordan",0,"","")
]

cursor.executemany("insert into BooksTable Values(?,?,?,?,?,?)", BookDetailsData)
connection.commit()

#============================================================================


#-------------------------------------------------------------------#
#                Create Employee Details Data                           #
# EmployeeTable                                                     #
# Employee_ID, Role, Name, Surname, DateOfBirth                     #
#-------------------------------------------------------------------#
EmployeeDetailsData =[
    ('JW820101','Cashier','John','Watson','1982-01-01'),
    ('SH840101','Finder','Sherlock','Holmes','1984-01-01'),
    ('GO820101','Packer','Greg','Officer','1982-01-01'),
    ('MW820101','Admin','Marry','Watson','1982-01-01')
    
]

cursor.executemany("insert into EmployeeTable Values(?,?,?,?,?)", EmployeeDetailsData)
connection.commit()

#============================================================================

#-------------------------------------------------------------------#
#                Create User Details Data                           #
# UserTable                                                         #    
# User_ID, Name, Surname, DateOfBirth                     #
#-------------------------------------------------------------------#
UserDetailsData =[
    (1,'James','May','1982-01-01'),
    (2,'Jeremy','Clarkson','1984-01-01'),
    (3,'Richard','Hammond','1982-01-01'),
    (4,'Sheldon','Cooper','1982-01-01')
    
]

cursor.executemany("insert into UserTable Values(?,?,?,?)", UserDetailsData)
connection.commit()

#============================================================================


connection.close()