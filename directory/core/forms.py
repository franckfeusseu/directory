from django import forms

from core.models import Company, Category, Contact

class CompanyFilterForm(forms.Form):
    description = forms.CharField(max_length=100)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    country = forms.ModelChoiceField(queryset=Contact.objects.values('country').distinct())
    city = forms.ModelChoiceField(queryset=Contact.objects.values('city').distinct())

class CompanySearchForm(forms.Form):
    query = forms.CharField(label='company', max_length=100)