from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from users.models import Author
from users.serializers import AuthorSerializer


class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
