from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("books/", BookViewSet.as_view({'get': 'get_books'})),
    path("books/<int:pk>/", BookViewSet.as_view({'get': 'get_selected_book'})),
    path("books/<int:pk>/read/", BookViewSet.as_view({'get': 'get_book_content'})),
]
