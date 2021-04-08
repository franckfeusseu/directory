import redis

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.postgres.search import SearchVector
from django.http import JsonResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.mail import send_mail

from core.common.decorators import ajax_required
from .models import Company, Person, Category, Contact, Follow, News
from .forms import CompanySearchForm
from .filters import CompanyFilter

r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

# Create your views here.
@login_required
def dashboard(request):
    user = request.user
    fcompany = user.companies.all()
    return render(request, 'core/dashboard.html', {'user':user, 'fcompany':fcompany})

def companysearch(request):
    form = CompanySearchForm()
    query = None
    results = []
    cresults = []
    if 'query' in request.GET:
        form = CompanySearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Company.objects.annotate(search=SearchVector('name'),).filter(search=query)
            cresults = Category.objects.annotate(search=SearchVector('cat_name'),).filter(search=query)
    return render(request, 'core/search.html', {'form':form, 'query': query, 'results': results, 'cresults': cresults})        

def directorsearch(request):
    form = CompanySearchForm()
    query = None
    results = []
    cresults = []
    if 'query' in request.GET:
        form = CompanySearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Person.objects.annotate(search=SearchVector('first_name'),).filter(search=query)
            cresults = Category.objects.annotate(search=SearchVector('cat_name'),).filter(search=query)
    return render(request, 'core/dsearch.html', {'form':form, 'query': query, 'results': results, 'cresults': cresults})        

def companyDetail(request, slug):
    company = get_object_or_404(Company, slug=slug)
    employes = company.employes.all()
    documents = company.documents.all()
    following = company.followers.all().count()
    company_categories_ids = company.categories.values_list('id', flat=True)
    similar_companies = Company.objects.filter(categories__in=company_categories_ids).exclude(id=company.id)
    news = News.objects.filter(company_linked=company)
    total_views = r.incr(f'company:{company.id}:views')
    r.zincrby('company_ranking', 1, company.id)
    return render(request, 'core/company_detail.html', {'company':company, 'employes':employes, 'documents':documents, 'similar_companies': similar_companies, 'following': following, 'news': news, 'total_views': total_views})

def companyCategoryList(request, slug):
    companies = Company.objects.all()
    if slug:
        cat = get_object_or_404(Category, slug=slug)
        companies = companies.filter(categories__in=[cat])[:120]
    return render(request, 'company_list.html', {'companies': companies,'cat':cat})

def home(request):
    return render(request, 'core/home.html')

def CompanyListView(request):
    companies = Company.objects.all()
    companiesNumber = companies.count()
    return render(request, 'company_list.html', {'companies': companies, 'companiesNumber': companiesNumber})

class PersonListView(ListView):
    model = Person
    template_name = 'core/person_list.html'

class PersonDetailView(DetailView):
    model = Person
    template_name = 'core/person_detail.html'
    slug_field = 'slug'

def category_chart(request):
    labels = []
    data = []

    queryset=Company.objects.values('categories').annotate(count=Count('categories')).distinct()
    for i in queryset:
        labels.append(Category.objects.get(id=i['categories']).cat_name)
        data.append(i['count'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

@ajax_required
@login_required
@require_POST
def user_follow(request):
    company_id = request.POST.get('id')
    action = request.POST.get('action')
    if company_id and action:
        try:
            company = Company.objects.get(id=company_id)
            if action == 'follow':
                Follow.objects.get_or_create(company=company, user=request.user)
            else:
                Follow.objects.filter(company=company, user=request.user).delete()
            return JsonResponse({'status': 'ok'})        
        except Company.DoesNotExist:
            return JsonResponse({'status':'error'})
    return JsonResponse({'status':'error'})

def company_ranking(request):
    company_ranking = r.zrange('company_ranking', 0, -1, desc=True)[:10]
    company_ranking_ids = [int(id) for id in company_ranking]
    most_viewed = list(Company.objects.filter(id__in= company_ranking_ids))
    most_viewed.sort(key=lambda x: company_ranking_ids.index(x.id))
    return render(request, 'company_rlist.html', {'most_viewed': most_viewed})    

def contact(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(subject, message, email, ['contact@veriskiq.com'])

        
    return render(request, 'core/contact.html')       