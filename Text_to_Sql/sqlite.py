import sqlite3

#connectting to Sqlite
connection=sqlite3.connect("student.db") #if db not exists it will create the db of same name

#create a cursor object to insert records,create table

cursor=connection.cursor() # it is responsible for traversing table and all records AND ALSO CREATING


## create the table 
table_info="""
Create table  STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25));
"""

cursor.execute(table_info)

##inserting some records

cursor.execute('''Insert Into Student values('Abhay','AI','A' )''')
cursor.execute('''Insert Into Student values('Ajay','AI','B' )''')
cursor.execute('''Insert Into Student values('Abhi','AI','A' )''')
cursor.execute('''Insert Into Student values('Abhishek','ML','A' )''')
cursor.execute('''Insert Into Student values('Akash','ML','A' )''')

#Displaying all the records

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for r in data:
    print(r)


connection.commit()
connection.close()