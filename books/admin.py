from django.contrib import admin

# Register your models here.
from books.models import Book, Order


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
