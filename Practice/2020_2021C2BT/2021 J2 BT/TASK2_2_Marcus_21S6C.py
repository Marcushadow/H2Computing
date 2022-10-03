import pymongo, os, json

mango = pymongo.MongoClient("127.0.0.1", 27017)
db = mango.get_database("Vaccine")
coll = db.get_collection("Staff")


print("Those who did not accept: ")
query = {"Acceptance":"No"}
result = coll.find(query)

for value in result:

    print(value["Name"], value["Age"], value["Reason"])


print("\nThose with at least one taken")
query = {"VacDates": {"$exists": True}}
result = coll.find(query)

print(result.count())

query = {"Name": "Charlie Lee"}
result = coll.find_one(query)["VacDates"]
update = {"$set": {"VacDates": [result, "5 Apr 2021"]}}

coll.update_one(query, update)



print("\nAbove 50 years 2 dose")

query = {"Age" : {"$gte": 50}, "VacDates" : {"$exists": True}}
result = coll.find(query)

for value in result:
    if len(value["VacDates"]) == 2:
        print(value)




mango.close()
