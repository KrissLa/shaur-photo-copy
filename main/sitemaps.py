from django.contrib.sitemaps import Sitemap
from .models import Main

class MainSitemap(Sitemap):
    """Получение главной страницы"""
    changefreq = 'daily'
    priority = 0.9
    location = '/'


    def items(self):
        return Main.objects.all().order_by('-id')[:1]

    def lastmod(self, obj):
        return obj.updated





