from django.contrib import admin

from .models import Book
from author.models import Author


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    # def get_author(self, obj):
    #     return ", ".join([Author.name for book in obj.author.all()])


admin.site.register(Book, BookAdmin)