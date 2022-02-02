# Generated by Django 3.0.8 on 2022-01-29 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=200)),
                ('cat_description', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('profile', models.TextField()),
                ('immatriculation_numb', models.CharField(max_length=200)),
                ('operating_status', models.CharField(choices=[('AC', 'Active'), ('DI', 'Dissolved'), ('LI', 'Liquidation'), ('DO', 'Dormant')], default='AC', max_length=2)),
                ('company_type', models.CharField(choices=[('PLC', 'public limited company'), ('LTD', 'private limited company'), ('STD', 'sole trader')], default='PLC', max_length=200)),
                ('founded_date', models.DateField()),
                ('dissolved_on', models.DateField(blank=True, null=True)),
                ('employees_numb', models.CharField(choices=[('MICRO', 'Less than 10'), ('SMALL', '10 - 50'), ('MEDIUM', '51 - 250'), ('LARGE', 'More than 250')], default='MICRO', max_length=10)),
                ('logo', models.ImageField(default='logo/default_logo.png', upload_to='logo/')),
                ('categories', models.ManyToManyField(related_name='companies', to='core.Category')),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('street', models.CharField(default='null', max_length=200)),
                ('house_number', models.IntegerField(blank=True, default=0, null=True)),
                ('postal_code', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('facebook_page', models.URLField(blank=True, null=True)),
                ('twitter_page', models.URLField(blank=True, null=True)),
                ('linkedin_page', models.URLField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
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
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Contact')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=200)),
                ('type_description', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name': 'type',
                'verbose_name_plural': 'types',
            },
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
                ('end', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to='core.Company')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to='core.Person')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('source', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('category_linked', models.ManyToManyField(blank=True, null=True, to='core.Category')),
                ('company_linked', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Company')),
            ],
            options={
                'verbose_name': 'news',
                'verbose_name_plural': 'news',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow', to='core.Company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateField(auto_now_add=True)),
                ('document', models.FileField(upload_to='documents')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='core.Company')),
                ('doc_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='core.Type')),
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
        migrations.AddField(
            model_name='company',
            name='followers',
            field=models.ManyToManyField(related_name='companies', through='core.Follow', to=settings.AUTH_USER_MODEL),
        ),
    ]
