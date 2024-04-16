from django import template
from django.contrib.auth.models import User

from ..utils import connect_to_mongodb
from ..models import Author

register = template.Library()


def get_user(id_):
    try:
        user = User.objects.get(id=id_)
        return user.username
    except User.DoesNotExist:
        return 'unknown'


register.filter('user', get_user)
