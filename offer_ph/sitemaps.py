from django.contrib.sitemaps import Sitemap
from .models import Offer

class OfferSitemap(Sitemap):
    """Страница 'Как заказать фотосъёмку'"""
    changefreq = 'daily'
    priority = 0.9
    location = '/how_to_order_photography/'


    def items(self):
        return Offer.objects.all().order_by('-id')[:1]

    def lastmod(self, obj):
        return obj.updated





