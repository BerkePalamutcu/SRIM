# Generated by Django 4.2 on 2023-05-18 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='date',
        ),
        migrations.AddField(
            model_name='conference',
            name='dateEnd',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='conference',
            name='dateStart',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='imgUrl',
            field=models.ImageField(upload_to=''),
        ),
    ]
