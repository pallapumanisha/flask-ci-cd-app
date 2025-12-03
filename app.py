from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Correct MongoDB connection for Docker Compose
mongo_uri = os.environ.get("MONGO_URI", "mongodb://mongo:27017/")
client = MongoClient(mongo_uri)

db = client["mydatabase"]          # database name
collection = db["mycollection"]    # collection name

# Home route
@app.route("/")
def home():
    return jsonify({"message": "Flask app updated with docker-compose!"})


# Insert data route
@app.route("/add")
def add_data():
    data = {"name": "Manisha", "task": "Flask Docker CI/CD"}
    collection.insert_one(data)
    return jsonify({"status": "success", "data": data})

# Fetch data route
@app.route("/data")
def get_data():
    documents = list(collection.find({}, {"_id": 0}))  # exclude internal Mongo _id
    return jsonify(documents)

# Main
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
