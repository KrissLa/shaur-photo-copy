from django.contrib.sitemaps import Sitemap
from .models import Review

class ReviewSitemap(Sitemap):
    """Страница с отзывами"""
    changefreq = 'daily'
    priority = 0.9
    location = '/reviews/'


    def items(self):
        return Review.objects.all().order_by('-id')[:1]

    def lastmod(self, obj):
        return obj.updated







