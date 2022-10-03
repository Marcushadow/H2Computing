import pymongo

client = pymongo.MongoClient("127.0.0.1", 27017)

db = client.get_database("library")
coll = db.get_collection("books")

query = {"year": "2015"}
result = coll.find(query)

print("All books published in 2015")
for item in result:
    print(item['book_id'], item['title'], item['author'])
    
query = {"page_count": {"$gte": 100, "$lt": 400}}
result = coll.find(query)


print("All books with pages greater or equal to 100 and less than 400")
for item in result:
    print(item)
    
query = {"page_count": {"$exists" : False}}
update = {"$set": {"page_count": "Less Than 100 Pages"}}
 
 
print("This is sorted:")
result = coll.find().sort("year")
#sortedDict = sorted(result, key = lambda x: x.get('year'), reverse = True)
#result = list(result)
#result.sort(key = lambda x: x.get('year'), reverse = True)

for item in result:
    print(item)

