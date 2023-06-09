# Generated by Django 4.2 on 2023-05-24 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0009_news_alter_bulletin_created_alter_person_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=399, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
                ('img_url', models.ImageField(blank=True, null=True, upload_to='')),
                ('link', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 16, 58, 36, 45993, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
