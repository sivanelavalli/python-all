import cx_Oracle
conn=cx_Oracle.connect("system","sivasp","localhost:1521/xe")
cursor=conn.cursor()
try:
    cursor.execute("insert into students values(105,'bagi',800)")
    conn.commit()
    print("Record is inserted")
except:
    conn.rollback()
    print("Record is already exists")
print("Program completed")
conn.close()
