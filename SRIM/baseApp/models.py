from django.db import models

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
