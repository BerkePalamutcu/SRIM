# Generated by Django 4.2 on 2023-06-06 21:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0024_alter_bulletin_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='member_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 21, 33, 6, 104703, tzinfo=datetime.timezone.utc)),
        ),
    ]