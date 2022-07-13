import pymongo, os, json

mango = pymongo.MongoClient("127.0.0.1", 27017)
db = mango.get_database("Vaccine")
coll = db.get_collection("Staff")


filepath = os.path.join("Additional Materials", "STAFF.json")


with open(filepath) as fs:
    data = json.load(fs)
    
coll.insert_many(data)
mango.close()