from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    pass


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    patronymic = models.CharField(max_length=64)

    @property
    def get_fio(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    @property
    def get_books_count(self):
        return self.books.all().count()
