from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .models import Place, Seo_places
from .forms import PlacesForm
# Create your views here.

class SeoPlacesView:
    """Получение SEO"""
    def get_seo_places(self):
        return Seo_places.objects.all()

    def get_last_place(self):
        return Place.objects.filter(published=True).order_by('-id')[:1]


class PlaceListView(SeoPlacesView, ListView):
    """Список всех мест"""
    model = Place
    template_name = 'places/place_list.html'

    def get_context_data(self, **kwargs):
        context = super(PlaceListView, self).get_context_data(**kwargs)
        context['place_list_1'] = Place.objects.filter(published=True).order_by('-id')
        context['form'] = PlacesForm()
        return context

class AddPlaces(View):
    """Добавление места через форму на сайте"""

    new_place = None
    def post(self, request):
        place_list_1 = Place.objects.filter(published=True).order_by('-id')
        form = PlacesForm(request.POST, request.FILES)
        if form.is_valid():
            new_place = form.save()
        else:
            form = PlacesForm()
        return render(request, 'places/places_was_added.html', {'new_place': new_place,
                                                          'place_list_1':place_list_1,
                                                          })