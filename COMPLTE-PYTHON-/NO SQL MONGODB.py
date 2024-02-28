import pymongo

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://New:new@cluster0.lidzegc.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
#try:
  #  client.admin.command('ping')
   # print("Pinged your deployment. You successfully connected to MongoDB!")
#except Exception as e:
 #   print(e)
'''uploading database from python to mongodb'''
'''single dictionary '''
data = {
    "name" : "Lenend",
    "mail_id" : "Legend@gmail.com",
    "subject" : ["data scinece" , "big data " , "data analytics "]
}
'''Creating a database '''
database = client['myinfo']#USING CONNECTIVITY WITH CLIENT DATABASE myinfo  CREATED
collection = database["swap"]# COLLECTION A BUNCH OF DATA OR DOCUMENT INSIDE A DATABASE, A TABLE INSIDE DATABASE
# INSIDE THAT TABLE WE WILL DUMP DATA
collection.insert_one(data)

'''inserting database from python to mongodb'''
'''multiple dictionary '''
'''json datasets- multiple ,nested dictionaries'''

list_of_records = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},

    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},

    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}
]
database = client['myinfo']#USING CONNECTIVITY WITH CLIENT DATABASE myinfo  CREATED
collection = database["swap"]# COLLECTION A BUNCH OF DATA OR DOCUMENT INSIDE A DATABASE, A TABLE INSIDE DATABASE
# INSIDE THAT TABLE WE WILL DUMP DATA
#collection.insert_one(data)
collection.insert_many(list_of_records)

'''inserting complex jason data to mongodb'''
data1 = {"packetType":"D","data":{"checkEngineLightFlag":"F","batteryVoltageStableTime":0,"batteryVoltageStable":"0","batteryVoltageOff":"12.42","batteryCrankParamTN":"-0.08","batteryCrankParamVN":"0.00","batteryCrankParamTP":"-0.08","batteryCrankParamVP":"0.00","batteryCrankParamTT":"-0.00008","batteryCrankParamV0":"0.00","batteryVoltageMaxOn":"13.05","batteryVoltageMinOn":"12.97","batteryVoltageMaxOff":"12.46","batteryVoltageMinOff":"12.36","batteryVoltageOnAverage":"13.02","engineLoadMax":"84","engineLoadAverage":"39.98","rpmMax":"3487","rpmAverage":"1431.29","gpsSpeedAverage":"21.99","vssMax":"53.44","vssAverage":"23.06","tcuTemperatureMin":"82.40","tcuTemperatureMax":"109.40","tcuTemperatureAverage":"104.87","coolantMin":"158.00","coolantMax":"188.60","coolantAverage":"180.20","packetStartLocal":1508143346000,"tripStartLocal":1508143346000,"milIndicator":"F","monitorsNotReady":0,"imei":"60DF5417","gatewayTs":1515613306592,"diagnosticTroubleCodeData":[345345],"diagnosticPidData":[[64768,47,100],[64768,1,517376],[64800,1,262144],[64768,5,125]]},"header":{"iwrapVer":"1.9.20","sourceSystem":"CDP","configVer":"1.1","oemName":"HUM","unitType":0,"cpVer":"7.50.1.9","igpsVer":"1.3.7","messageType":"Notification","pomVer":"1.0","headerVer":"V6","timestamp":0,"deviceType":"InDrive","visorVer":"1.4.35","transactionId":"53098471-7787-4160-94b3-cd69dcc70416","deviceSerialNo":"60DF5417","subOrganization":"HUM","organization":"HUM","imei":"60DF5417","operation":"Notification"}}

database = client['myinfo']#USING CONNECTIVITY WITH CLIENT DATABASE myinfo  CREATED
collection = database["swap"]# COLLECTION A BUNCH OF DATA OR DOCUMENT INSIDE A DATABASE, A TABLE INSIDE DATABASE
# INSIDE THAT TABLE WE WILL DUMP DATA
#collection.insert_one(data)
collection.insert_one(data1)


'''creating a table in mongodb '''
pkt = {"packetType":"D","data":{"checkEngineLightFlag":"F","batteryVoltageStableTime":0,"batteryVoltageStable":"0","batteryVoltageOff":"12.42","batteryCrankParamTN":"-0.08","batteryCrankParamVN":"0.00","batteryCrankParamTP":"-0.08","batteryCrankParamVP":"0.00","batteryCrankParamTT":"-0.00008","batteryCrankParamV0":"0.00","batteryVoltageMaxOn":"13.05","batteryVoltageMinOn":"12.97","batteryVoltageMaxOff":"12.46","batteryVoltageMinOff":"12.36","batteryVoltageOnAverage":"13.02","engineLoadMax":"84","engineLoadAverage":"39.98","rpmMax":"3487","rpmAverage":"1431.29","gpsSpeedAverage":"21.99","vssMax":"53.44","vssAverage":"23.06","tcuTemperatureMin":"82.40","tcuTemperatureMax":"109.40","tcuTemperatureAverage":"104.87","coolantMin":"158.00","coolantMax":"188.60","coolantAverage":"180.20","packetStartLocal":1508143346000,"tripStartLocal":1508143346000,"milIndicator":"F","monitorsNotReady":0,"imei":"60DF5417","gatewayTs":1515613306592,"diagnosticTroubleCodeData":[345345],"diagnosticPidData":[[64768,47,100],[64768,1,517376],[64800,1,262144],[64768,5,125]]},"header":{"iwrapVer":"1.9.20","sourceSystem":"CDP","configVer":"1.1","oemName":"HUM","unitType":0,"cpVer":"7.50.1.9","igpsVer":"1.3.7","messageType":"Notification","pomVer":"1.0","headerVer":"V6","timestamp":0,"deviceType":"InDrive","visorVer":"1.4.35","transactionId":"53098471-7787-4160-94b3-cd69dcc70416","deviceSerialNo":"60DF5417","subOrganization":"HUM","organization":"HUM","imei":"60DF5417","operation":"Notification"}}

database = client['myinfo']#USING CONNECTIVITY WITH CLIENT DATABASE myinfo  CREATED
collection = database["add_data"]# COLLECTION A BUNCH OF DATA OR DOCUMENT INSIDE A DATABASE, A TABLE INSIDE DATABASE
# INSIDE THAT TABLE WE WILL DUMP DATA
#collection.insert_one(data)
collection.insert_one(pkt)

'''within one table able to store different different type of documents or any kind of docs '''
'''no need to worry about schema of the table'''
'''inside one collection different type of docs, different type of dataset, any kind of data  '''
'''document bases database'''



'''to check every information '''
record = collection.find()
for i in record:
    print(i)

    '''extraction of specific data'''
    collection.find({"companyName":"iNeuron" })
    for i in data:
        print(i)

    collection.find({"couseOffered":{"$gt":"E"}})
    for i in data:
        print(i)

'''extraction of data as per specific conditions'''

import pymongo
data2 =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]


uri = "mongodb+srv://New:new@cluster0.lidzegc.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
database = client['inventory']
collection = database["table"]
collection.insert_many(data2)
d=collection.find()#like select * from table
for i in d:
    print(i)

'''filter operations'''

d=collection.find({"status ":"A"})#status should be A
for i in d:
    print(i)


d = collection.find({'status':{'$in':['A' , 'P']}})#either A or P
for i in d:
    print(i)

d = collection.find({'status':{"$gt" : "C"}})#status should be grater than B
for i in d:
    print(i)

d = collection.find({'qty':{'$gte' :75}})#should be grether than 75
for i in d:
    print(i)

d = collection.find({'item': 'sketch pad','qty': 95})#and conditon
for i in d:
    print(i)

d = collection.find({ 'item': 'sketch pad' , 'qty' :{"$gte" : 75}})#and conditon

for i in d:
    print(i)

d = collection.find({'$or' : [{ 'item': 'sketch pad'} , {'qty': {"$gte": 75}}]})#or condition
for i in d:
    print(i)


'''updation of data'''
collection.update_one({'item': 'canvas'} , {'$set':{'item': 'Swapnil'} })

d = collection.find({'item':'Swapnil'})#recheck the data
for i in d:
    print(i)
#collection.delete_one({'item': 'Swapnil'})#to delete the data


