from django.urls import path

from . import views

urlpatterns = [

    path('', views.PriceListView.as_view(), name='price_list'),
    path('<slug:slug>/', views.PriceDetailView.as_view(), name='price_detail'),

]