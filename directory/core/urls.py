from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('search', views.search, name='search'),
    path('dsearch', views.directorsearch, name='dsearch'),
    path('companies', views.CompanyListView, name='companies'),
    path('persons', views.PersonListView.as_view(), name='persons'),
    path('company/<slug:slug>', views.companyDetail, name='company_detail'),
    path('person/<slug:slug>', views.PersonDetailView.as_view(), name='person_detail'),
    path('category/<slug:slug>', views.companyCategoryList, name='company_category_list'),
    path('category-chart/', views.category_chart, name='category_chart'),
    path('follow/', views.user_follow, name='user_follow'),
    path('companyranking', views.company_ranking, name='ranking'),
    path('pricing', TemplateView.as_view(template_name="core/pricing.html"), name='pricing'),
    path('about', TemplateView.as_view(template_name="core/about.html"), name='about'),
    path('reports', TemplateView.as_view(template_name="core/reports.html"), name='reports'),
    path('market-research', TemplateView.as_view(template_name="core/market-research.html"), name='market-research'),
    path('risk-management', TemplateView.as_view(template_name="core/risk-management.html"), name='risk-management'),
    path('data-solution', TemplateView.as_view(template_name="core/data-solution.html"), name='data-solution'),
    path('contact', views.contact, name='contact'),
]