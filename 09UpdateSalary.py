from pymongo import MongoClient

try:
    client=MongoClient("mongodb://localhost:27017")
    db=client["office"]
    coll=db["workers"]

    qr={}
    id=int(input('Enter Employee ID : '))
    qr["_id"]=id

    upval={}
    colnm=int(input('Enter New Salary : '))
    upval["salary"]=colnm

    upd={"$set":upval}

    coll.update_one(qr,upd)

    print("Salary Updated Successfully..")


except:
    print("ID Not Found..")