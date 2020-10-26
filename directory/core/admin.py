from django.contrib import admin

from core.models import Contact, Telephone, Company, Category, Person, Role, Document, Type, Follow, News
# Register your models here.
admin.site.register(Contact)
admin.site.register(Telephone)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Person)
admin.site.register(Role)
admin.site.register(Type)
admin.site.register(Document)
admin.site.register(Follow)
admin.site.register(News)
