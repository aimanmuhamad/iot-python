import pymongo
import random
import time

#Create database
client = pymongo.MongoClient("mongodb://localhost:xxxx/"")
database = client['MeasurementSystem']
collection = database["MeasurementData"]

Ts = 10
N = 10
for k in range(N):
    LowLimit = 20
    UpperLimit = 25
    MeasurementValue = random.randint(LowLimit,UpperLimit)

    now = datetime.now()
    datetimeformat = "%Y-%m-%d %H:%M:%S"
    measurementdatetime = now.strftime(datatimeformat)

    #Insert data to database
    document = {"MeasurementValue" : MeasurementValue, "MeasurementDateTime": measurementdatetime }
    x = x = collection.insert_one(document)
    time.sleep(Ts)