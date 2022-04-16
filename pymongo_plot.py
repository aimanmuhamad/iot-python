import pymongo
import matplotlib.pyplot as plt
from datetime import datetime

#Connect database
client = pymongo.MongoClient("mongodb://localhost:xxxx/"")
database = client['MeasurementSystem']
collection = database["MeasurementData"]

t = []
data = []

for document in collection.find():
    MeasurementValue = document["MeasurementValue"]
    MeasurementDateTime = document["MeasurementDateTime"]

    timeformat = "%Y-%m-%d %H:%M:%S"
    MeasurementDateTime = datetime.strptime(MeasurementDateTime,timeformat)

    data.append(MeasurementValue)
    t.append(MeasurementDateTime)

#Plotting
plt.plot(t,data,'o-')
plt.title("Temperature")
plt.xlabel('t[s]')
plt.ylabel('Temp[C]')
plt.grid()
plt.show()