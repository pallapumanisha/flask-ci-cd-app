from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB using docker-compose service name "mongo"
client = MongoClient("mongodb://mongo:27017")
db = client["testdb"]
collection = db["messages"]

@app.route('/')
def index():
    # Insert sample data if not exists
    collection.insert_one({"msg": "Hello from MongoDB!"})

    # Read last inserted
    data = collection.find().sort("_id", -1).limit(1)[0]
    return f"Flask + MongoDB Connected Successfully → {data['msg']}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
