from django.contrib import admin

# Register your models here.

from .models import Conference, Bulletin, Person


@admin.register(Conference, Bulletin, Person)
class AuthorAdmin(admin.ModelAdmin):
    pass
