# Generated by Django 3.0.8 on 2020-07-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200721_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='employees_numb',
            field=models.CharField(choices=[('MICRO', 'Less than 10'), ('SMALL', '10 - 50'), ('MEDIUM', '51 - 250'), ('LARGE', 'More than 250')], default='MICRO', max_length=10),
        ),
    ]
