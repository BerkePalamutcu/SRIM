# Generated by Django 4.2 on 2023-05-20 03:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0006_bulletin_created_alter_bulletin_bulletinmagazine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 20, 3, 3, 25, 767664, tzinfo=datetime.timezone.utc)),
        ),
    ]
