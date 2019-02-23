import sqlite3 as sql

conn=sql.connect("mydatabase.db")
curs=conn.cursor()
name=input("Enter emp name: ")
curs.execute("delete from employees where name=?",(name,))
conn.commit()
print("Employee" +name+ " is deleted")
conn.close()