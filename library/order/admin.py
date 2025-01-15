from django.contrib import admin

from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_book_id', 'get_user_id', 'created_at', 'end_at','plated_end_at')

    def get_book_id(self, obj):
        return obj.book.id

    get_book_id.short_description = 'Book ID'

    def get_user_id(self, obj):
        return obj.user.id

    get_user_id.short_description = 'User ID'


admin.site.register(Order, OrderAdmin)