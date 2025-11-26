from flask import Flask
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

app = Flask(__name__)

@app.route("/")
def home():
    try:
        # Connect to MongoDB on localhost:27017
        client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
        client.admin.command("ping")  # Check MongoDB
        message = "MongoDB server is successfully installed via Docker CI/CD 🚀 8907"

    except ConnectionFailure:
        message = "Failed to connect to MongoDB server. chittamma"
    finally:
        try:
            client.close()
        except Exception:
            pass

    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
