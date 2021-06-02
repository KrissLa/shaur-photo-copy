
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.


class SeoPriceView:
    """Получение SEO"""
    def get_seo_price(self):
        return Seo_price.objects.all()



class PriceView:
    """Список цен на всех страницах с ценами"""

    def get_price_list(self):
        return Price.objects.all().order_by('id')



class PriceListView(SeoPriceView, ListView):
    """Список цен"""
    model = Price
    queryset = Price.objects.all().order_by('id')


class PriceDetailView(PriceView, DetailView):
    """Страница с прайсом"""
    model = Price
    slug_field = 'url'
