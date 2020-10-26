# Generated by Django 3.0.8 on 2020-07-20 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=200)),
                ('cat_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profile', models.TextField()),
                ('immatriculation_numb', models.CharField(max_length=200)),
                ('operating_status', models.CharField(choices=[('AC', 'Active'), ('DI', 'Dissolved'), ('LI', 'Liquidation'), ('DO', 'Dormant')], default='AC', max_length=2)),
                ('company_type', models.CharField(max_length=200)),
                ('founded_date', models.DateField()),
                ('dissolved_on', models.DateField()),
                ('employees_numb', models.CharField(max_length=200)),
                ('categories', models.ManyToManyField(to='core.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('facebook_page', models.URLField()),
                ('twitter_page', models.URLField()),
                ('linkedin_page', models.URLField()),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('dob', models.DateField()),
                ('nationality', models.CharField(max_length=200)),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel_number', models.CharField(max_length=50)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to='core.Company')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to='core.Person')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='contact',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Contact'),
        ),
        migrations.AddField(
            model_name='company',
            name='employes',
            field=models.ManyToManyField(through='core.Role', to='core.Person'),
        ),
    ]
