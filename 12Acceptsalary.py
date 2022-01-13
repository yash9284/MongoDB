from pymongo import MongoClient

try:
    client=MongoClient("mongodb://localhost:27017")
    db=client["office"]
    coll=db["workers"]

    qr={}
    salary=int(input('Enter Employee Salary : '))
    qr["salary"]=salary

   
    for doc in coll.find():
       print(doc)


except:
    print("Not Found..")

       