# Generated by Django 4.2 on 2023-05-19 00:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0005_bulletin'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletin',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 0, 52, 37, 620134)),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='bulletinMagazine',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]