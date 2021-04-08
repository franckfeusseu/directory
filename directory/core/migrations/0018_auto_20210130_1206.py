# Generated by Django 3.0.8 on 2021-01-30 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20201006_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='logo/default_logo.png', upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='facebook_page',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='linkedin_page',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='twitter_page',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
