# Generated by Django 4.2 on 2023-06-06 22:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0025_members_member_img_alter_bulletin_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='workgroup',
            name='coordinator_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 22, 37, 32, 585950, tzinfo=datetime.timezone.utc)),
        ),
    ]