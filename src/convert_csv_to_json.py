import csv
import json

# Define input and output file paths
csv_data = "../data/airbnb_listings.csv"
json_data = "../data/airbnb_listings.json"

# Columns to exclude from the output JSON
exclude_columns = {"license", "neighbourhood_group"}

# Convert CSV to JSON
data = []
with open(csv_data, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        # Remove empty columns
        row = {key: value for key, value in row.items() if key not in exclude_columns}

        # Clean and convert fields to appropriate data types
        row['id'] = int(row['id'])
        row['host_id'] = int(row['host_id'])
        row['latitude'] = float(row['latitude'])
        row['longitude'] = float(row['longitude'])
        row['price'] = float(row['price']) if row['price'] else None
        row['minimum_nights'] = int(row['minimum_nights']) if row['minimum_nights'] else 0
        row['number_of_reviews'] = int(row['number_of_reviews']) if row['number_of_reviews'] else 0

        # Handle missing values
        row['last_review'] = row['last_review'] if row['last_review'] else None
        row['reviews_per_month'] = float(row['reviews_per_month']) if row['reviews_per_month'] else 0.0

        row['calculated_host_listings_count'] = int(row['calculated_host_listings_count'])
        row['availability_365'] = int(row['availability_365']) if row['availability_365'] else 0
        row['number_of_reviews_ltm'] = int(row['number_of_reviews_ltm']) if row['number_of_reviews_ltm'] else 0

        data.append(row)

# Write the JSON file
with open(json_data, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Successfully converted CSV to JSON: {json_data}")
