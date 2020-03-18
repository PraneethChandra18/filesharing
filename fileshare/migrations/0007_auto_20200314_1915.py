# Generated by Django 3.0.1 on 2020-03-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0006_auto_20200314_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.FileField(max_length=50, upload_to=''),
        ),
    ]