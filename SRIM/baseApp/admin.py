from django.contrib import admin

# Register your models here.

from .models import Conference, Bulletin, Person, News, Archive, Status


@admin.register(Conference, Bulletin, Person, News, Archive, Status)
class AuthorAdmin(admin.ModelAdmin):
    pass
