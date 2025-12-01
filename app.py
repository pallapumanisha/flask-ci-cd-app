from flask import Flask
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os

iapp = Flask(__name__)

@app.route("def home():
    client = None
    try:
        # Use MONGO_URI from environment if present, else default to Docker service name "mongo"
        mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=2000)

        # Ping MongoDB to confirm the connection works
        client.admin.command("ping")

        message = "MongoDB server is successfully installed via Docker compose CI/CD new555"
    except ConnectionFailure:
        message = "Failed to connect to MongoDB server. Badam Psst"
    except Exception as e:
        # Optional: print exact error to container logs for debugging
        print(f"Unexpected error while connecting to MongoDB: {e}")
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

