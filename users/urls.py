from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import AuthorListView

app_name = 'users'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authors/', AuthorListView.as_view(), name='author-list'),

]
