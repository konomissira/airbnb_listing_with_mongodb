# FastAPI & MongoDB API

This project is a REST API built with FastAPI and MongoDB, allowing CRUD operations on Airbnb listings. The API is tested using Postman.

## Features

• GET - Retrieve all listings or a specific listing by ID.

• POST - Create a new listing.

• PUT - Update an existing listing.

• DELETE - Remove a listing from the database.

## Technologies Used

• FastAPI - A high-performance web framework for building APIs.

• MongoDB - A NoSQL database for storing listing data.

• Pymongo - A Python driver for MongoDB.

• Uvicorn - ASGI server for running FastAPI applications.

## Installation

1 Clone the repository

• git clone https://github.com/konomissira/airbnb_listing_with_mongodb.git

• cd airbnb_listing_with_mongodb

2 Create a virtual environment

• python3 -m venv .venv

• source .venv/bin/activate # macOS/Linux

• .venv\Scripts\activate # Windows

3 Install dependencies

• pip install fastapi uvicorn pymongo

4 Ensure MongoDB is running locally

## Dataset Preparation (Airbnb Listings)

1 Download the Airbnb dataset (CSV format)

• Get the dataset from Inside Airbnb from the following url:
https://insideairbnb.com/fr/get-the-data/

2 Convert CSV to JSON

• The dataset needs to be converted from CSV to JSON format before inserting into MongoDB.

• A script csv_to_json.py has been provided in the project to handle this conversion.

• Run the script:

python src/csv_to_json.py

3 Load Data into MongoDB

• After converting the dataset to JSON, it needs to be inserted into MongoDB.

• A script insert_data.py is available to automate this process.

• Run the script:

python src/insert_data.py

4 Verify in MongoDB

use airbnb_db
db.listings.findOne()

## Running the API

uvicorn src.main:app --reload

## API Endpoints

### Testing with Postman

• Postman is used to send HTTP requests and test API endpoints.

• Open Swagger UI for interactive documentation at: http://127.0.0.1:8000/docs

1 Get All Listings

• GET http://127.0.0.1:8000/listings

2 Get a Specific Listing by ID

• GET http://127.0.0.1:8000/listings/{listing_id}

3 Create a New Listing

• POST http://127.0.0.1:8000/listings
Request Body (JSON):
{
"name": "Modern Apartment in London Bridge",
"host_name": "Jane",
"neighbourhood": "Camden",
"room_type": "Entire home/apt",
"price": 120,
"minimum_nights": 3,
"availability_365": 200
}

4 Update a Listing

• PUT http://127.0.0.1:8000/listings/{listing_id}
Request Body (JSON):
{
"price": 150,
"availability_365": 365
}

5 Delete a Listing

• DELETE http://127.0.0.1:8000/listings/{listing_id}
Removes a listing from the database.

### Next Steps

• Add request validation with Pydantic.

• Implement error handling and pagination.

• Secure the API with authentication (JWT tokens).
