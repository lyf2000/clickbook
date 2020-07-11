from rest_framework import serializers

from books.models import Book
from users.models import Author


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'cost')


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    fio = serializers.ReadOnlyField(source='get_fio')
    books_count = serializers.ReadOnlyField(source='get_books_count')

    class Meta:
        model = Author
        fields = ('id', 'fio', 'books_count', 'books')
