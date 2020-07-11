from django.contrib import admin

from users.models import User, Author


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
