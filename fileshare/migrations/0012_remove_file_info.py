# Generated by Django 3.0.1 on 2020-03-19 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0011_auto_20200319_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='info',
        ),
    ]
