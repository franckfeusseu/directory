# Generated by Django 3.0.8 on 2020-10-06 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200921_1717'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'company', 'verbose_name_plural': 'companies'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'contact', 'verbose_name_plural': 'contacts'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'person', 'verbose_name_plural': 'persons'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'type', 'verbose_name_plural': 'types'},
        ),
    ]
