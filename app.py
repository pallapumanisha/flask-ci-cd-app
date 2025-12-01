from flask import Flask
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os

app = Flask(__name__)

@app.route("/")
def home():
    client = None
    try:
        # Read MongoDB URI from environment variable, fallback to service name 'mongo'
        mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=2000)
        client.admin.command("ping")  # Ping MongoDB to ensure connection

        message = "MongoDB server is successfully installed via Docker compose CI/CD 9090 🚀"
    except ConnectionFailure:
        message = "Failed to connect to MongoDB server. Badam Psst"
    finally:
        if client:
            try:
                client.close()
            except Exception:
                pass

    return message


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
