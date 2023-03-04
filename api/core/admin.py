from django.contrib import admin
from .models import Book, Genre, Author, AgeRestrictions, UserBook


class BookAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    pass


class AgeRestrictionsAdmin(admin.ModelAdmin):
    pass


class UserBookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, BookAdmin)
admin.site.register(Author, BookAdmin)
admin.site.register(AgeRestrictions, BookAdmin)
admin.site.register(UserBook, UserBookAdmin)
