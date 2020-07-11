from django.contrib.auth import get_user_model
from rest_framework import serializers

from books.models import Book
from users.models import Author

User = get_user_model()


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


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = ('username', 'password',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
