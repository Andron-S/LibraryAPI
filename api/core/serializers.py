from rest_framework import serializers
from .models import Book, Author, Genre
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="name", queryset=Author.objects.all())
    genre = serializers.SlugRelatedField(slug_field="title", queryset=Genre.objects.all())

    class Meta:
        model = Book
        fields = ("title", "genre", "author", "image")







