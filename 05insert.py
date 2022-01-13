from pymongo import MongoClient

try :
    client=MongoClient("mongodb://localhost:27017")
    db=client["office"]
    coll=db["workers"]

    dic={}
    id=int(input('Enter ID : '))
    empnm=input('Enter Name : ')
    dept=input('Enter Department: ')
    post=input('Enter Post: ')
    city=input('Enter City: ')
    salary=int(input('Enter Salary: '))
    mobile=int(input('Enter Mobile Number: '))
    email=input('Enter Email:')
    
    dic["_id"]=id
    dic["empnm"]=empnm
    dic["dept"]=dept
    dic["post"]=post
    dic["city"]=city
    dic["salary"]=salary
    dic["mobile"]=mobile
    dic["email"]=email

    coll.insert_one(dic)
    print('Data of new employee inserted successfully..')

except:
    print("Error")