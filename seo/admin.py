from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import ConnectSSModel, CounterForSite


@admin.register(ConnectSSModel)
class ConnectSSModelAdmin(admin.ModelAdmin):
    """Поисковые системы"""
    list_display = ("name", 'published')
    list_editable = ('published',)


@admin.register(CounterForSite)
class CounterForSiteAdmin(admin.ModelAdmin):
    """Счечики и аналитика для сайта"""
    list_display = ("name", "published")
    list_editable = ('published',)
