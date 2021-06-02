from django.urls import path

from . import views

urlpatterns = [
    path('', views.Offer_liListView.as_view(), name='offer_ph'),
    path('offer_added/', views.OfferAdd.as_view(), name='add_offer'),
]
