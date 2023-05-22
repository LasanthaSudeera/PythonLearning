from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
database = client['python_learning']

# Collection is similar to table
collection = database['product']

product1 = {
    "name": "iPhone",
    "price": "1500"
}

# Insert one
# collection.insert_one(product1)

product_collction = [
    {
        "name": "nokia 105",
        "price": "100"
    },
    {
        "name": "google pixel",
        "price": "500"
    }
]

# Insert a collection
# collection.insert_many(product_collction)

# Find by a field match
result = collection.find_one({"name": "google pixel"})
print(result)

# Find by ID
result = collection.find_one({"_id": ObjectId('6469b29b800aa64a2359dfe4')})
print(result)

# Update Operation
collection.update_one({"_id": ObjectId('6469b29b800aa64a2359dfe4')}, {
                      "$set": {"price": 300}})

# Delete Operation
collection.delete_one({"_id": ObjectId('6469b29b800aa64a2359dfe3')})