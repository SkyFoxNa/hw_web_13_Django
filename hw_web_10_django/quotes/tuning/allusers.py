import os
import django
import random
from django.contrib.auth.models import User

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_web_10_django.settings")
# django.setup()


def all_users():
    # Получаем все объекты пользователей из базы данных Django
    return User.objects.all()