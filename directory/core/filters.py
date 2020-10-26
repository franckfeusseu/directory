from core.models import Company

import django_filters

class CompanyFilter(django_filters.FilterSet):
    class Meta:
        model = Company
        fields = ['company_type', 'categories']