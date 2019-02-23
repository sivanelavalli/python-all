import pymongo
conn=pymongo.MongoClient(host='localhost',port=27017)
db=conn.test123
collection=db.student
collection.insert_one({'sid':101,'sname':'siva','password':'sivas','marks':900})
collection.insert_one({'sid':102,'sname':'srinu','password':'srinus','marks':900,'group':'csc'})
print("Documents are inserted")
conn.close()