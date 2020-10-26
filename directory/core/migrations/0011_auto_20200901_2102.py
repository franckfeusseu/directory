# Generated by Django 3.0.8 on 2020-09-01 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200827_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(blank=True, max_length=250),
        ),
    ]
