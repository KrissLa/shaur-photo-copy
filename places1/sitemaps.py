from django.contrib.sitemaps import Sitemap
from .models import Place

class PlaceSitemap(Sitemap):
    """Страница с местами"""
    changefreq = 'daily'
    priority = 0.9
    location = '/place/'


    def items(self):
        return Place.objects.filter(published=True).order_by('-id')[:1]

    def lastmod(self, obj):
        return obj.updated





