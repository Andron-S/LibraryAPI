from rest_framework import serializers
from .models import Book, Author
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from django.contrib.auth.models import User


class BookSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="name", queryset=Author.objects.all())
    genreList = TagListSerializerField()

    class Meta:
        model = Book
        fields = ("title", "genre", "author", "image")




