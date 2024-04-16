from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# Create a model of authors.
class Author(models.Model):
    fullname = models.CharField(max_length = 50)
    born_date = models.CharField(max_length = 50)
    born_location = models.CharField(max_length = 150)
    description = models.TextField()
    created_at = models.DateField(auto_now_add = True)

    def __str__(self) :
        return f"{self.fullname}"


# Create a model of tags.
class Tag(models.Model):
    name = models.CharField(max_length = 50, null = False, unique = False)

    def __str__(self) :
        return f"{self.name}"


# Create a model of quotes.
class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, default = None, null = True)
    created_at = models.DateField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None, null = True)
