import os
import django
import random
# from django.contrib.auth.models import User

from pymongo import MongoClient
from .conects import connect_mongodb

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_web_10_django.settings")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_web_10_django.settings')
django.setup()

from quotes.models import Author, Tag, Quote, User  # noqa

db = connect_mongodb()  # Підключення до  MongoDB з файлу connects

authors = db.authors.find()
print(authors)

for author in authors :
    print(author['fullname'])
    Author.objects.get_or_create(
        fullname = author['fullname'],
        born_date = author['born_date'],
        born_location = author['born_location'],
        description = author['description']
    )

# Получаем все объекты пользователей из базы данных Django
all_users = User.objects.all()

quotes = db.quotes.find()

for quote in quotes :
    # Случайным образом выбираем пользователя из списка всех пользователей
    random_user = random.choice(all_users)
    # random_user = random.randint(1, 4)

    tags = []
    for tag in quote['tags'] :
        t, *_ = Tag.objects.get_or_create(name=tag)
        print(t)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote = quote['quote'])))

    if not exist_quote :
        author = db.authors.find_one({'_id' : quote['author']})
        a = Author.objects.get(fullname = author['fullname'])
        q = Quote.objects.create(
            quote = quote['quote'],
            author = a,
            user = random_user  # Связываем случайного пользователя с цитатой
        )

        for tag in tags:
            q.tags.add(tag)
