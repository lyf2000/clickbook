from rest_framework.generics import ListAPIView

from books.models import Book
from books.serializers import BookSerializer


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
