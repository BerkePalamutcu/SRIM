# Generated by Django 4.2 on 2023-06-06 20:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0020_alter_bulletin_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=99)),
                ('member_workgroup', models.CharField(max_length=99, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=399)),
                ('coordinator', models.CharField(max_length=199)),
                ('instution', models.CharField(max_length=399)),
                ('location', models.CharField(max_length=199)),
                ('email', models.CharField(max_length=99)),
            ],
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 20, 51, 0, 911663, tzinfo=datetime.timezone.utc)),
        ),
    ]