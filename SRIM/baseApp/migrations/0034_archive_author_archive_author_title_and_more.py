# Generated by Django 4.2 on 2023-06-08 00:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0033_archive_author_img_alter_bulletin_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='archive',
            name='author',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
        migrations.AddField(
            model_name='archive',
            name='author_title',
            field=models.CharField(blank=True, max_length=299, null=True),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 8, 0, 34, 57, 241864, tzinfo=datetime.timezone.utc)),
        ),
    ]