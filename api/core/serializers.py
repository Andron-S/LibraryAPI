from rest_framework import serializers
from .models import Book, Author, Genre, UserBook
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="name", queryset=Author.objects.all())
    genre = serializers.SlugRelatedField(slug_field="title", queryset=Genre.objects.all())

    class Meta:
        model = Book
        fields = ("title", "genre", "author", "image")


class SelectedBookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="name", queryset=Author.objects.all())
    genre = serializers.SlugRelatedField(slug_field="title", queryset=Genre.objects.all())

    class Meta:
        model = Book
        fields = ("title", "genre", "author", "pageNumber", "restriction", "image", "description")


class BookContentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="name", queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ("title", "author", "content")


class UserBookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="name", queryset=Author.objects.all())
    genre = serializers.SlugRelatedField(slug_field="title", queryset=Genre.objects.all())
    title = serializers.SlugRelatedField(slug_field="title", queryset=Book.objects.all())
    image = serializers.SlugRelatedField(slug_field="image", queryset=Book.objects.all())

    class Meta:
        model = UserBook
        fields = ("genre", "author", "title", "image")

    def create(self, validated_data):
        pass
