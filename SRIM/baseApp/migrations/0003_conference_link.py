# Generated by Django 4.2 on 2023-05-18 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0002_remove_conference_date_conference_dateend_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='link',
            field=models.TextField(null=True),
        ),
    ]