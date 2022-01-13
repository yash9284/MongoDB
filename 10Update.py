from pymongo import MongoClient

try:
    client=MongoClient("mongodb://localhost:27017")
    db=client["office"]
    coll=db["workers"]

    qr={}
    id=int(input('Enter Employee ID : '))
    qr["_id"]=id

    upval={}
    colnm1=input('Enter New City : ')
    colnm2=input('Enter New Department : ')

    upval["city"]=colnm1
    upval["dept"]=colnm2

    upd={"$set":upval}

    coll.update_one(qr,upd)
    print("City and Department updated...")


except:
    print("Not Found..")