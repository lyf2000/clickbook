from rest_framework import serializers

from books.models import Book
from users.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    fio = serializers.ReadOnlyField(source='get_fio')

    class Meta:
        model = Author
        fields = ('id', 'fio')


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('id', 'name', 'cost', 'author')
