from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId
from typing import List

# Initialize FastAPI
app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["airbnb_db"]
collection = db["listings"]

# Helper function to convert MongoDB object to JSON
def serialize_document(doc):
    doc["_id"] = str(doc["_id"])  # Convert ObjectId to string
    return doc

# ------------------- API Endpoints -------------------

# 1. Get all listings
@app.get("/listings", response_model=List[dict])
def get_listings():
    listings = collection.find().limit(10)
    return [serialize_document(listing) for listing in listings]

# 2. Get a single listing by ID
@app.get("/listings/{listing_id}")
def get_listing(listing_id: str):
    listing = collection.find_one({"_id": ObjectId(listing_id)})
    if listing:
        return serialize_document(listing)
    return {"error": "Listing not found"}

# 3. Add a new listing
@app.post("/listings")
def create_listing(listing: dict):
    result = collection.insert_one(listing)
    return {"message": "Listing added", "id": str(result.inserted_id)}

# 4. Update a listing by ID
@app.put("/listings/{listing_id}")
def update_listing(listing_id: str, updated_data: dict):
    result = collection.update_one({"_id": ObjectId(listing_id)}, {"$set": updated_data})
    if result.matched_count:
        return {"message": "Listing updated"}
    return {"error": "Listing not found"}

# 5. Delete a listing by ID
@app.delete("/listings/{listing_id}")
def delete_listing(listing_id: str):
    result = collection.delete_one({"_id": ObjectId(listing_id)})
    if result.deleted_count:
        return {"message": "Listing deleted"}
    return {"error": "Listing not found"}

# ------------------- Run Server -------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
