import sqlite3

## Connect to sqlite 
connection=sqlite3.connect("student.db")

## Create a cursor object to insert record, create table 
cursor=connection.cursor()

##CReate the table 
table_info=""" 
create table STUDENT(NAME VARCHAR(20), CLASS VARCHAR(25),
SECTION VARCHAR(10), MARKS INT)
"""

cursor.execute(table_info)

## Inserting some records in the table
cursor.execute('''Insert into STUDENT values('Vansh','Chemical Eng','A',67)''')
cursor.execute('''Insert into STUDENT values('Harsh Yadav','Civil Eng','B',99)''')
cursor.execute('''Insert into STUDENT values('Abhijit Patil','Agricultural Eng','C',88)''')
cursor.execute('''Insert into STUDENT values('Manish patil','Data Science','D',100)''')

## Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data :
    print(row)

## Commit the changes in the database 
connection.commit()
connection.close()

