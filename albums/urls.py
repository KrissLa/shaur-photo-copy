from django.urls import path

from . import views

urlpatterns = [

    path('', views.albums_list, name='albums_list'),
    # path('', views.product_list, name='product_list'),
    path('<slug:photography_slug>/', views.albums_list, name='albums_list_by_photography'),
    path('<int:albums_id>/<slug:slug>/share/', views.album_share, name='albums_share'),
    path('<int:id>/<slug:slug>/', views.AlbumDetailView.as_view(), name='albums_detail'),

]
