import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='root',db='test',port=3306)
cursor=conn.cursor()
cursor.execute("create table testemployees(eid int(5)primary key,ename varchar(10),salary int(10))")
print("Table is created")
cursor.execute("insert into employees values(111,'siva',80000)")
cursor.execute("insert into employees values(222,'srinu',50000)")
print("2 rows inserted")
conn.commit()
conn.close()