from django.db import models
from django.utils.timezone import now
from django.urls import reverse
import json
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


class SliderContent(models.Model):
    title = models.CharField(max_length=399)
    location = models.CharField(max_length=99, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    month_start = models.CharField(null=True, max_length=39)
    month_end = models.CharField(null=True, max_length=39)
    img_url = models.ImageField(null=True, blank=True)
    image_content = models.BooleanField()
    event_link = models.TextField(null=True, blank=True)
    event_description = models.TextField(null=True, blank=True)
    blog_post = models.BooleanField()
    pdf_content = models.BooleanField(default=False)
    pdf_file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title


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


class News(models.Model):
    name = models.CharField(max_length=399, null=True)
    description = models.TextField(null=True, blank=True)
    document = models.FileField(null=True, blank=True)
    img_url = models.ImageField(null=True, blank=True)
    news_link = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Archive(models.Model):
    name = models.CharField(max_length=399, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    document = models.FileField(null=True, blank=True)
    img_url = models.ImageField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    author_img = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=99, blank=True, null=True)
    author_title = models.CharField(max_length=299, blank=True, null=True)
    content = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('archive', args=[str(self.id)])

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=99, null=True, blank=True)
    document = models.FileField()

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=99, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    content = models.TextField()
    post_img = models.ImageField(null=True, blank=True)
    author_img = models.ImageField(null=True, blank=True)
    author_title = models.CharField(max_length=299, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])


class Members(models.Model):
    member_name = models.CharField(max_length=99)
    workshop_list = models.TextField(null=True, blank=True)
    member_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.member_name


class WorkGroup(models.Model):
    name = models.CharField(max_length=399)
    coordinator = models.CharField(max_length=199)
    coordinator_img = models.ImageField(null=True, blank=True)
    instution = models.CharField(max_length=399, null=True, blank=True)
    instution_image = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=199, null=True, blank=True)
    location_image = models.ImageField(null=True, blank=True)
    email = models.CharField(max_length=99)

    def __str__(self):
        return self.name


class AnteriorRomedInf(models.Model):
    name = models.CharField(max_length=99)
    year = models.CharField(max_length=4)
    location = models.CharField(max_length=99)
    event_link = models.TextField(null=True, blank=True)
    event_document = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name


class EchipaTitles(models.Model):
    title = models.CharField(max_length=199)
    name = models.CharField(max_length=299)
    image = models.ImageField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    instution = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
