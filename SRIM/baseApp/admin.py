from django.contrib import admin

# Register your models here.

from .models import Conference, Bulletin, Person, News, Archive, Status, SliderContent, BlogPost, Members, WorkGroup, AnteriorRomedInf, EchipaTitles


@admin.register(Conference, Bulletin, Person, News, Archive, Status, SliderContent, BlogPost, Members, WorkGroup, AnteriorRomedInf, EchipaTitles)
class AuthorAdmin(admin.ModelAdmin):
    pass
