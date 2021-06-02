from django.contrib.sitemaps import Sitemap
from .models import Price

class PriceSitemap(Sitemap):
    """Страница со списком цен"""
    changefreq = 'daily'
    priority = 0.9
    location = '/price/'


    def items(self):
        return Price.objects.all().order_by('-id')[:1]

    def lastmod(self, obj):
        return obj.updated

class PriceDetailSitemap(Sitemap):
    """Все страница с ценами"""
    changefreq = 'daily'
    priority = 0.9


    def items(self):
        return Price.objects.all()

    def lastmod(self, obj):
        return obj.updated





