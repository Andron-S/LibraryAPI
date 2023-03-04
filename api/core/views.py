from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from .serializers import BookSerializer, SelectedBookSerializer, BookContentSerializer, UserBookSerializer
from .models import Book, UserBook
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


class UserBookViewSet(viewsets.ModelViewSet):
    serializer_class = UserBookSerializer
    queryset = UserBook.objects.all()
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['get'])
    def get_user_book(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['delete'])
    def delete_user_book(self, request, pk):
        book = UserBook.objects.filter(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def add_user_book(self, request, pk):
        queryset_book = Book.objects.filter(pk=pk)

        if len(queryset_book) == 0:
            return Response({
                'error': "Такой книги не существует"
            }, status=status.HTTP_400_BAD_REQUEST)

        user_book = UserBook.objects.filter(book=queryset_book[0], user=request.user)

        if len(user_book) > 0:
            return Response({
                'error': "Такая книга уже добавлена"
            })

        added_book = UserBookSerializer(data=request.data, context={
            'user': request.user,
            'book': queryset_book[0],
        })

        if added_book.is_valid():
            added_book.save()
            return Response(added_book.data, status=status.HTTP_201_CREATED)
        return Response(added_book.errors, status=status.HTTP_400_BAD_REQUEST)




