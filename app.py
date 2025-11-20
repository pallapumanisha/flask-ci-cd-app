from flask import Flask
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

app = Flask(__name__)

@app.route("/")
def home():
    try:
        client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
        client.admin.command("ping")
        message = "MongoDB server is successfully installed"
    except ConnectionFailure:
        message = "Failed to connect to MongoDB server"
    finally:
        try:
            client.close()
        except Exception:
            pass

    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
