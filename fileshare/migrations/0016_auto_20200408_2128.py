# Generated by Django 3.0.1 on 2020-04-08 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0015_auto_20200323_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
