# Generated by Django 3.0.8 on 2020-07-21 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200720_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='house_number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='street',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
