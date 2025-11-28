from flask import Flask
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
import time

app = Flask(__name__)

@app.route("/")
def home():
    client = None
    mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017/")

    # Retry logic
    max_retries = 10
    sleep_time = 2
    for attempt in range(max_retries):
        try:
            client = MongoClient(mongo_uri, serverSelectionTimeoutMS=2000)
            client.admin.command("ping")
            return "MongoDB server is successfully installed via Docker Compose CI/CD 🚀"
        except ConnectionFailure:
            print(f"Attempt {attempt+1}/{max_retries}: MongoDB not ready yet...")
            time.sleep(sleep_time)
        finally:
            if client:
                try:
                    client.close()
                except:
                    pass

    return "Failed to connect to MongoDB server. Badam Psst"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
