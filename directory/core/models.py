from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings

# import django country model
from django_countries.fields import CountryField


# Create your models here.
class Contact(models.Model):
    country = CountryField()
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    street = models.CharField(max_length=200, default='null')
    house_number = models.IntegerField(default=0, blank=True, null=True)
    postal_code = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    facebook_page = models.URLField(max_length=200, null=True, blank=True)
    twitter_page = models.URLField(max_length=200, null=True, blank=True)
    linkedin_page = models.URLField(max_length=200, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return '{} {}'.format(self.house_number, self.street)


class Telephone(models.Model):
    tel_number = models.CharField(max_length=50)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.tel_number)


class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    cat_description = models.TextField()
    slug = models.SlugField(max_length=250, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.cat_name)
        super().save(*args, **kwargs) 

    def __str__(self):
        return '{}'.format(self.cat_name)

    def get_absolute_url(self):
        return reverse('core:company_category_list', args=[self.slug])


class Type(models.Model):
    type_name = models.CharField(max_length=200)
    type_description = models.TextField()
    slug = models.SlugField(max_length=250, blank=True)

    class Meta:
        verbose_name = 'type'
        verbose_name_plural = 'types'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.type_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.type_name)             


class Person(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Other'),
    ]

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    nationality = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, blank=True)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'persons'

    def save(self, *args, **kwargs):
        full_name = self.first_name + "" + self.last_name
        if not self.slug:
            self.slug = slugify(full_name)
        super().save(*args, **kwargs) 

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('core:person_detail', args=[self.slug])   
    

class Company(models.Model):

    ACTIVE = 'AC'
    DISSOLVED = 'DI'
    LIQUIDATION = 'LI'
    DORMANT = 'DO'
    COMPANY_STATUS =[
        (ACTIVE, 'Active'),
        (DISSOLVED, 'Dissolved'),
        (LIQUIDATION, 'Liquidation'),
        (DORMANT, 'Dormant'),
    ]

    MICRO = 'MICRO'
    SMALL = 'SMALL'
    MEDIUM = 'MEDIUM'
    LARGE = 'LARGE'
    COMPANY_SIZE = [
        (MICRO, 'Less than 10'),
        (SMALL, '10 - 50'),
        (MEDIUM, '51 - 250'),
        (LARGE, 'More than 250'),
    ]

    PUBLIC_LIMITED_COMPANY = 'PLC'
    PRIVATE_LIMITED_COMPANY = 'LTD'
    ONE_PERSON_COMPANY = 'STD'
    COMPANY_TYPE = [
        (PUBLIC_LIMITED_COMPANY, 'public limited company'),
        (PRIVATE_LIMITED_COMPANY, 'private limited company'),
        (ONE_PERSON_COMPANY, 'sole trader'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, blank=True)
    profile = models.TextField()
    immatriculation_numb = models.CharField(max_length=200)
    operating_status = models.CharField(max_length=2, choices=COMPANY_STATUS, default=ACTIVE)
    company_type = models.CharField(max_length=200, choices=COMPANY_TYPE, default=PUBLIC_LIMITED_COMPANY)
    founded_date = models.DateField()
    dissolved_on = models.DateField(blank=True, null=True)
    employees_numb = models.CharField(max_length=10, choices=COMPANY_SIZE, default=MICRO)
    employes = models.ManyToManyField(Person, through='Role')
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='companies')
    logo = models.ImageField( upload_to="logo/", default='logo/default_logo.png')
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Follow', related_name='companies')

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('core:company_detail', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Document(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    document = models.FileField(upload_to='documents')
    doc_type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='documents')        


class Role(models.Model):
    position = models.CharField(max_length=200)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    company = models.ForeignKey(Company, related_name='role', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, related_name='role', on_delete=models.CASCADE)


class Follow(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='follow', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='follow', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f'{self.user} follows {self.company}'   


class News(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    source = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    company_linked = models.OneToOneField(Company, on_delete=models.CASCADE, null=True, blank=True)
    category_linked = models.ManyToManyField(Category, null=True, blank=True)

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
    


