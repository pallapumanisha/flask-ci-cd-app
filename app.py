from flask import Flask
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os

app = Flask(__name__)

@app.route("/")
def home():
    client = None
    try:
        # Read from env variable (set in docker-compose.yml), fallback to mongo service
        mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
        # Connect to MongoDB inside Docker network (service name: mongo)
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=2000)
        client.admin.command("ping")  # Check MongoDB is reachable

        message = "MongoDB server is successfully installed via Docker compose.yml CI/CD 🚀"

    except ConnectionFailure:
        message = "Failed to connect to MongoDB server. chittamma"
    finally:
        if client is not None:
            try:
                client.close()
            except Exception:
                pass

    return message


if __name__ == "__main__":
    # Flask listens on all interfaces, port 5000 (inside the container)
    app.run(host="0.0.0.0", port=5000)
