import pymongo
client = pymongo.MongoClient("mongodb+srv://Sreetej98:Sree9866*#@cluster0.kagw2yv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


#import pymongo
#client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
#db = client.test
#print(db)

d = {
    "name" : "sreeteja",
    "email" : "sreeteja@gmail.com",
    "surname" : "vadla"
}
d = {
    "name" : "sreeteja",
    "email" : "sreeteja@gmail.com",
    "surname" : "vadla"
}
d = {
    "name" : "sreeteja",
    "email" : "sreeteja@gmail.com",
    "surname" : "vadla"
}
d = {
    "name" : "sreeteja",
    "email" : "sreeteja@gmail.com",
    "surname" : "vadla"
}


db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

