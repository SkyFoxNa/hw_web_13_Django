from pymongo import MongoClient
from mongoengine import connect, disconnect


def connect_to_mongodb():
    # disconnect()

    # Подключение к MongoDB
    client = MongoClient("mongodb+srv://user_goit_web:user_goit_web@mains-db.nfj7rrz.mongodb.net/?retryWrites=true&w=majority"
               "&appName=Mains-db")

    db = client.hw_web_10_django
    return db
