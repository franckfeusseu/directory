# Generated by Django 3.0.8 on 2020-07-28 06:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_company_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
