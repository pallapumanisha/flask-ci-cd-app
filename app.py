from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongo:27017/")
db = client["testdb"]
collection = db["testcollection"]

@app.route("/")
def home():
    collection.insert_one({"message": "Hello from Flask and MongoDB!"})
    return "Flask + MongoDB connection successful! using docker-compose"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
