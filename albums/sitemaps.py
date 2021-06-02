from django.contrib.sitemaps import Sitemap
from .models import Photography, Albums

class PhotographySitemap(Sitemap):
    """Страница со всеми альбомами"""
    changefreq = 'daily'
    priority = 0.9
    location = '/albums/'


    def items(self):
        return Photography.objects.filter(published=True).order_by('-id')[:1]


class PhotographyDetailSitemap(Sitemap):
    """Фотосъёмки"""
    changefreq = 'daily'
    priority = 0.9


    def items(self):
        return Photography.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated



class AlbumsSitemap(Sitemap):
    """Все страницы с альбомами"""
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Albums.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated
