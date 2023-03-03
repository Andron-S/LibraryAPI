from rest_framework import viewsets, permissions, status
from .serializers import BookSerializer
from .models import Book
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_books(self, request):
        queryset = Book.objects.all()
        return Response(queryset, status=status.HTTP_200_OK)

