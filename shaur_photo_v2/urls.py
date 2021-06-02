"""shaur_photo_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from albums.sitemaps import PhotographySitemap, AlbumsSitemap, PhotographyDetailSitemap
from blog.sitemaps import PostSitemap, PostDetailSitemap
from main.sitemaps import MainSitemap
from offer_ph.sitemaps import OfferSitemap
from places1.sitemaps import PlaceSitemap
from price.sitemaps import PriceSitemap, PriceDetailSitemap
from reviews.sitemaps import ReviewSitemap

sitemaps = {'main': MainSitemap,
            'photography': PhotographySitemap,
            'photography_detail': PhotographyDetailSitemap,
            'albums': AlbumsSitemap,
            'blog': PostSitemap,
            'blog_detail': PostDetailSitemap,
            'offer': OfferSitemap,
            'place': PlaceSitemap,
            'price': PriceSitemap,
            'price_detail': PriceDetailSitemap,
            'reviews': ReviewSitemap,
            }

urlpatterns = [
    path('3773ex6/', admin.site.urls),

    path('nested_admin/', include('nested_admin.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),


    path('', include('main.urls')),
    path('albums/', include('albums.urls')),
    path('price/', include('price.urls')),
    path('blog/', include('blog.urls')),
    path('places/', include('places1.urls')),
    path('reviews/', include('reviews.urls')),
    path('how_to_order_photography/', include('offer_ph.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "SHAUR-PHOTO.COM"
admin.site.site_header = "Светлана Гавриловец   - shaur-photo.com"
