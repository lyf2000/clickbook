from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from books.models import Book, Order
from books.serializers import BookSerializer, OrderCreateSerializer
from books.tasks import order_book


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = (IsAuthenticated, )
    
    def create(self, request, *args, **kwargs):
        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_kwargs = serializer.validated_data
        order = Order.objects.create(**order_kwargs, client=request.user)
        order_book(order.id)
        headers = self.get_success_headers(serializer.data)
        return Response({}, status=status.HTTP_201_CREATED, headers=headers)