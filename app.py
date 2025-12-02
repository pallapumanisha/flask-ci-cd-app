from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(mongo_uri)
db = client["mydatabase"]          # database name
collection = db["mycollection"]    # collection name

# Default route
@app.route("/")
def home():
    return jsonify({"message": "Flask app is running!"})

# Example route to insert a document
@app.route("/add")
def add_data():
    data = {"name": "Manisha", "task": "Flask Docker CI/CD"}
    collection.insert_one(data)
    return jsonify({"status": "success", "data": data})

# Example route to fetch data
@app.route("/data")
def get_data():
    documents = list(collection.find({}, {"_id": 0}))  # exclude Mongo _id
    return jsonify(documents)

if __name__ == "__main__":
    # Run Flask app on all interfaces (important for Docker)
    app.run(host="0.0.0.0", port=5000, debug=True)

