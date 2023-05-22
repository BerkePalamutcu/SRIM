from django.db import models
from django.utils.timezone import now
# Create your models here.


class Conference(models.Model):
    dateStart = models.DateField(null=True)
    dateEnd = models.DateField(null=True)
    name = models.CharField(max_length=99)
    description = models.TextField()
    link = models.TextField(null=True)
    imgUrl = models.ImageField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Bulletin(models.Model):
    name = models.CharField(max_length=99)
    bulletinMagazine = models.FileField(null=True)
    created = models.DateTimeField(default=now())

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=99, null=True)
    title = models.CharField(max_length=49, null=True)
    role = models.CharField(max_length=99, null=True, blank=True)
    organization = models.CharField(max_length=99, null=True)
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
