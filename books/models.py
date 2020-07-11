from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    author = models.ForeignKey('users.Author', on_delete=models.CASCADE, related_name='books')
    name = models.CharField(max_length=256)
    cost = models.PositiveIntegerField()

    def clean(self):
        if self.cost == 0:
            raise ValidationError(
                _('Zero-cost book is not available!')
            )


class Order(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.SET_NULL, related_name='orders', null=True)
    client = models.ForeignKey('users.User', on_delete=models.SET_NULL, related_name='orders', null=True)
    call = models.PositiveIntegerField()
    comment = models.CharField(max_length=256, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
