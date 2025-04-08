from pymongo import MongoClient
import traceback

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
db = client['octofit']

# Test with a supported query
try:
    # Insert a test record into a collection
    test_collection = db['test_collection']
    test_collection.insert_one({"name": "Test Record"})
    print("Successfully inserted a record into the test collection.")

    # Query the test collection
    record = test_collection.find_one()
    print(f"Queried record: {record['name']}")
except Exception as e:
    print(f"Database operation failed: {e}")
    traceback.print_exc()
