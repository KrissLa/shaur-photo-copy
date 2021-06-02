from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    """Получение страницы со списком статей"""
    changefreq = 'daily'
    priority = 0.9
    location = '/blog/'


    def items(self):
        return Post.objects.filter(published=True).order_by('-id')[:1]

class PostDetailSitemap(Sitemap):
    """Получение всех страниц со статьями"""
    changefreq = 'daily'
    priority = 0.9


    def items(self):
        return Post.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated

