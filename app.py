from flask import Flask
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

app = Flask(__name__)

@app.route("/")
def home():
    client = None
    try:
        # 👉 Connect to MongoDB using the service name "mongo"
        client = MongoClient("mongodb://mongo:27017/", serverSelectionTimeoutMS=2000)
        client.admin.command("ping")  # Check MongoDB
        message = "MongoDB server is successfully installed via Docker compose.yml CI/CD 🚀"

    except ConnectionFailure:
        message = "Failed to connect to MongoDB server. chittamma"
    finally:
        if client:
            try:
                client.close()
            except Exception:
                pass

    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
