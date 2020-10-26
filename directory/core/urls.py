from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('search', views.search, name='search'),
    path('companies', views.CompanyListView, name='companies'),
    path('company/<slug:slug>', views.companyDetail, name='company_detail'),
    path('person/<slug:slug>', views.PersonDetailView.as_view(), name='person_detail'),
    path('category/<slug:slug>', views.companyCategoryList, name='company_category_list'),
    path('category-chart/', views.category_chart, name='category_chart'),
    path('follow/', views.user_follow, name='user_follow'),
    path('companyranking', views.company_ranking, name='ranking'),
    path('pricing', TemplateView.as_view(template_name="core/pricing.html"), name='pricing'),

]