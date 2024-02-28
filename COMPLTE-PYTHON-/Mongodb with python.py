'''Install monngodb packages'''
'''pip install pymongo'''

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://New:new@cluster0.lidzegc.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

d = {
    "name":"Swapnil Gosavi",
    "email" : "Swapnil.gosavi01@gmail.com",
    "surname" : "Gosavi"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
