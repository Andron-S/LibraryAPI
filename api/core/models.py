import datetime
from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)


class Genre(models.Model):
    title = models.CharField(max_length=32, blank=False, null=False, unique=True)


class Book(models.Model):
    genre = models.ForeignKey(to=Genre, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(to=Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, blank=False, null=False, unique=True)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=False, null=False)


class UserBook(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    date_added = models.DateField(default=datetime.date.today)
