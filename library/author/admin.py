from django.contrib import admin

from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'get_books')

    def get_books(self, obj):
        return ", ".join([book.name for book in obj.books.all()])
    get_books.short_description = 'Books'


admin.site.register(Author, AuthorAdmin)
