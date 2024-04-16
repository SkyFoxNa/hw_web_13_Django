import subprocess

# Запускаем команду
result = subprocess.run(['python3', '-m', 'tuning.migration'], capture_output=True, text=True)

# Печатаем вывод команды
print(result.stdout)

# Печатаем ошибки (если они есть)
print(result.stderr)
#
# from mongoengine import connect, disconnect
# from pymongo import MongoClient
# import environ
# import os
#
# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )
#
#
# def connect_to_mongodb():
#     # disconnect()
#
#     # Подключение к MongoDB
#     connect(
#         db = "hw_web_10_django",
#         host = "mongodb+srv://user_goit_web:user_goit_web@mains-db.nfj7rrz.mongodb.net/?retryWrites=true&w=majority"
#                "&appName=Mains-db",
#     )
#
#
# def connect_mongodb():
#     # disconnect()
#
#     # Подключение к MongoDB
#     client = MongoClient("mongodb+srv://user_goit_web:user_goit_web@mains-db.nfj7rrz.mongodb.net/?retryWrites=true&w=majority"
#                "&appName=Mains-db")
#
#     db = client.hw_web_10_django
#     return db


