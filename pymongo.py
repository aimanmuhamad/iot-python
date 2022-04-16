import pymongo

client = pymongo.MongoClient("mongodb://localhost:xxxx/"")
database = client['Library']
collection = database["Book"]

#Insert one document
document = ("Title" : "C# Programming", "Author" : "Knut")
x = collection.insert_one(document)

#Insert multiple documents
documents = [
    {"Title" : "C# Programming", "Author" : "Knut"},
    {"Title" : "ASP.NET", "Author" : "Henrik Ibsen"},
    {"Title" : "Python", "Author" : "Peter"}
]
x = collection.insert_many(document)

#SELECT data
#Can use find_one or find
x = collection.find_one()
print(x)

#Update data
query = {"Title" : "C# Programming"}
newvalue =  {"$set": {"Title" : "C# Web Programming"}}

collection.update_one(query,newvalue)

documents = collection.find()

for x in documents:
    print(x)