# Generated by Django 4.2 on 2023-06-06 21:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0023_remove_members_member_workgroup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 21, 29, 44, 151346, tzinfo=datetime.timezone.utc)),
        ),
    ]