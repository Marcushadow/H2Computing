import pymongo, os, json
client = pymongo.MongoClient("127.0.0.1", 27017)

db = client.get_database("library")
coll = db.get_collection("books")

filepath = os.path.join("Additional Material", "BOOK.txt")



with open(filepath) as file:
    data = file.read()
    contents = data.split("\n")
    
for i in range(len(contents)):
    contents[i] = json.loads(contents[i])

coll.insert_many(contents)
result = coll.find()

for entry in result:
    print(entry)

client.close()	

