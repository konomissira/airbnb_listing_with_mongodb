import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['airbnb_db']
collection = db['listings']

# Read JSON data from the file
file_path = "../data/airbnb_listings.json"
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Insert the data into the collection
if isinstance(data, list):
    collection.insert_many(data)
else:
    collection.insert_one(data)

print("Data successfully inserted into MongoDB!")