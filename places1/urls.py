from django.urls import path

from places1 import views

urlpatterns = [

    path('', views.PlaceListView.as_view(), name='places_list'),
    path('place_added/', views.AddPlaces.as_view(), name='add_place'),

]
