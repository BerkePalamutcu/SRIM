# Generated by Django 4.2 on 2023-06-06 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0022_alter_bulletin_created_alter_workgroup_instution_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='member_workgroup',
        ),
        migrations.AddField(
            model_name='members',
            name='workshop_list',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 21, 27, 41, 303675, tzinfo=datetime.timezone.utc)),
        ),
    ]
