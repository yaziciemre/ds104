from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Access a database
db = client['example_database']

# Access a collection
collection = db['example_collection'] # Table ==> collection

# Insert a document
document = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
}
insert_result = collection.insert_one(document)
print(f"Inserted document ID: {insert_result.inserted_id}")

# Insert multiple documents
documents = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "Bob", "age": 27, "email": "bob@example.com"}
]
insert_many_result = collection.insert_many(documents)
print(f"Inserted document IDs: {insert_many_result.inserted_ids}")

# Query the collection
query = {"name": "John Doe"}
result = collection.find_one(query)
print(f"Found document: {result}")

# Query all documents in the collection
all_documents = collection.find()
for doc in all_documents:
    print(doc)

# Update a document
update_query = {"name": "John Doe"}
new_values = {"$set": {"age": 31}}
update_result = collection.update_one(update_query, new_values)
print(f"Updated {update_result.modified_count} document(s)")

# Delete a document
delete_query = {"name": "John Doe"}
delete_result = collection.delete_one(delete_query)
print(f"Deleted {delete_result.deleted_count} document(s)")
