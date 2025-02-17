from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["airbnb_db"]
collection = db["listings"]

# --------- CREATE: Insert a new listing ----------
def insert_listing():
    new_listing = {
        "name": "Nice Studio in Central London",
        "host_name": "Jane",
        "neighbourhood": "Westminster",
        "room_type": "Entire home/apt",
        "price": 99,
        "minimum_nights": 3,
        "availability_365": 180
    }
    result = collection.insert_one(new_listing)
    print(f"Inserted document with ID: {result.inserted_id}")

# --------- READ: Fetch listings ----------
def get_listings():
    print("\nFetching listings under £100:")
    listings = collection.find({"price": {"$lt": 100}}).limit(5)
    for listing in listings:
        print(listing)

# --------- UPDATE: Modify an existing listing ----------
def update_listing():
    filter_query = {"name": "Nice Studio in Central London"}
    update_query = {"$set": {"price": 89}}
    result = collection.update_one(filter_query, update_query)
    print(f"Matched {result.matched_count} document(s) and modified {result.modified_count} document(s)")

# --------- DELETE: Remove a listing ----------
def delete_listing():
    filter_query = {"name": "Nice Studio in Central London"}
    result = collection.delete_one(filter_query)
    print(f"Deleted {result.deleted_count} document(s)")

# --------- Main Execution ----------
if __name__ == "__main__":
    insert_listing()  # Create
    get_listings()    # Read
    update_listing()  # Update
    delete_listing()  # Delete
