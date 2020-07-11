from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import Author
from users.serializers import AuthorSerializer, UserCreateSerializer


class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UserCreateView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        AllowAny  # Or anon users can't register
    ]
    serializer_class = UserCreateSerializer
