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
