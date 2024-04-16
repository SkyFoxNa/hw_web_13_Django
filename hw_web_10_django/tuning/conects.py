from mongoengine import connect, disconnect
from pymongo import MongoClient
from pathlib import Path

import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


def connect_to_mongodb():
    disconnect()

    # Подключение к MongoDB
    connect(
        db = f"{env("NAME_DB_MONGO")}",
        host = f"mongodb+srv://{env("USER_DB_MONGO")}:{env("PASSWORD_DB_MONGO")}@{env("SERVER_DB_MONGO")}",
    )


def connect_mongodb():
    disconnect()

    # Подключение к MongoDB
    # connections = f"mongodb+srv://{env("USER_DB_MONGO")}:{env("PASSWORD_DB_MONGO")}@{env("SERVER_DB_MONGO")}"
    connections = f"mongodb+srv://{env("USER_DB_MONGO")}:{env("PASSWORD_DB_MONGO")}@{env("SERVER_DB_MONGO")}"
    client = MongoClient(connections)
    clients = f'{env("NAME_DB_MONGO")}'
    # print(client)

    db = client.clients
    # print(db1)
    # print("______________")
    # # Подключение к MongoDB
    # client = MongoClient("mongodb+srv://user_goit_web:user_goit_web@mains-db.nfj7rrz.mongodb.net/?retryWrites=true&w=majority"
    #            "&appName=Mains-db")
    # print(client)
    # db = client.hw_web_10_django
    # print(db)
    return db


