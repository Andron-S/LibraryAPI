from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action

from .serializers import BookSerializer, SelectedBookSerializer, BookContentSerializer
from .models import Book
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['get'])
    def get_books(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def get_selected_book(self, request, pk):
        book = self.queryset.get(pk=pk)
        serializer = SelectedBookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def get_book_content(self, request, pk):
        book = self.queryset.get(pk=pk)
        serializer = BookContentSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)






