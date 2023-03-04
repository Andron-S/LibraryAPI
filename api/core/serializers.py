from rest_framework import serializers
from .models import Book, Author, Genre, UserBook
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="name", queryset=Author.objects.all())
    genre = serializers.SlugRelatedField(slug_field="title", queryset=Genre.objects.all())

    class Meta:
        model = Book
        fields = ("id", "title", "genre", "author", "image")


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
    title = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    genre = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = UserBook
        fields = ("id", "title", "author", "genre", "image")

    @staticmethod
    def get_title(user_book):
        return user_book.book.title

    @staticmethod
    def get_author(user_book):
        return user_book.book.author.name

    @staticmethod
    def get_genre(user_book):
        return user_book.book.genre.title

    @staticmethod
    def get_image(user_book):
        return user_book.book.image.url

    def create(self, validated_data):
        return UserBook.objects.create(**validated_data, **self.context)
