from pymongo import MongoClient
from datetime import datetime

# If using local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# If using MongoDB Atlas replace with your connection string:
# client = MongoClient("your_connection_string_here")

db = client["login_app"]
users_collection = db["users"]

def register_user(username, password):
    user = {
        "username": username,
        "password": password,
        "created_at": datetime.now()
    }
    users_collection.insert_one(user)

def login_user(username, password):
    return users_collection.find_one({
        "username": username,
        "password": password
    })