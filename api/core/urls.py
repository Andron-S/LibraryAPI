from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserBookViewSet

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("books/", BookViewSet.as_view({'get': 'get_books'})),
    path("books/select/<int:pk>/", BookViewSet.as_view({'get': 'get_selected_book'})),
    path("books/read/<int:pk>/", BookViewSet.as_view({'get': 'get_book_content'})),
    path("books/my/", UserBookViewSet.as_view({'get': 'get_user_book'})),
    path("books/my/<int:pk>/delete/", UserBookViewSet.as_view({'delete': 'delete_user_book'})),
    path("books/my/<int:pk>/add/", UserBookViewSet.as_view({'post': 'add_user_book'})),
]
