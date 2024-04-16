from bson.objectid import ObjectId
from django import template
from django.contrib.auth.models import User

from ..utils import connect_to_mongodb
from ..models import Author

register = template.Library()

#
# def get_author_mongodb(id_):
#     db = connect_to_mongodb()
#     author = db.authors.find_one({'_id': ObjectId(id_)})
#     return author['fullname']


def get_author(id_):
    author = Author.objects.get(id=id_)
    return author.fullname


register.filter('author', get_author)
