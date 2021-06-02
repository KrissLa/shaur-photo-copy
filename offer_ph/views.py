from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.base import View
from .forms import OfferForm

from .models import *


# Create your views here.


class Offer_liListView(ListView):
    """Страница 'Как заказать фотосъёмку'"""
    model = Offer_li
    template_name = 'offer_ph/offer_ph_detail.html'
    queryset = Offer_li.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super(Offer_liListView, self).get_context_data(**kwargs)
        context['offer'] = Offer.objects.filter(published=True)
        context['form'] = OfferForm()
        return context


class OfferAdd(View):
    """Добавление места через форму на сайте"""
    def post(self, request):
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = OfferForm()
        return render(request, 'offer_ph/offer_added.html')
