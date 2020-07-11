from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from books.views import BookListView
from users.views import AuthorListView

app_name = 'books'

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),

]
