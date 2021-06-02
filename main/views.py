from django.shortcuts import render
from django.views.generic import ListView
from .models import Main
from albums.models import Photography, Albums
from blog.models import Post
from reviews.models import Review
from offer_ph.forms import OfferForm
# Create your views here.


class ObjectsAll:
    """Получение объектов из других приложений"""

    def get_last_album(self):
        """Последний альбом"""
        return Albums.objects.filter(published=True).filter(album_to_index=True).order_by('-publish')[:1]

    def get_photography(self):
        """Список фотосъёмок"""
        return Photography.objects.filter(published=True).order_by('id')

    def get_reviews(self):
        """Список отзывов"""
        return Review.objects.filter(published=True).filter(to_main=True)

    def get_post_2(self):
        """Последние 2 статьи"""
        return Post.objects.filter(published=True).order_by('-id')[:2]

    def get_post(self):
        """Последняя статья"""
        return Post.objects.filter(published=True).order_by('-id')[:1]


class MainView(ObjectsAll, ListView):
    """Вывод главной страницы"""
    model = Main
    template_name = 'main/index1.html'
    # template_name = 'main/tech_work.html'
    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['form'] = OfferForm()
        return context



