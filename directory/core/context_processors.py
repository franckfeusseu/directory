import redis

from django.conf import settings
from .models import Company


r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

def company_ranking(request):
    company_ranking = r.zrange('company_ranking', 0, -1, desc=True)[:10]
    company_ranking_ids = [int(id) for id in company_ranking]
    most_viewed = list(Company.objects.filter(id__in= company_ranking_ids))
    most_viewed.sort(key=lambda x: company_ranking_ids.index(x.id))
    return {'most_viewed': most_viewed}