from django.contrib import admin
from .models import Offer, Offer_li, OfferPhotography


# Register your models here.


class OfferLiAdmin(admin.StackedInline):
    """Ссылка на соц сеть"""
    model = Offer_li
    extra = 3


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    """Регистрация страница 'Как заказать фотосъёмку'"""
    model = Offer
    inlines = [OfferLiAdmin, ]
    save_on_top = True


@admin.register(OfferPhotography)
class OfferAddAdmin(admin.ModelAdmin):
    """Регистрация заказов в админке"""
    model = OfferPhotography
    save_on_top = True
    readonly_fields = (
    'id', 'name', 'phone_number', 'photography', 'comment', 'сity', 'time_to_call_1', 'time_to_call_2',
    'date_of_photography', 'added')
    list_display = ('id', 'name', 'phone_number', 'сity', 'new_offer', 'viewed', 'your_list', 'added')
    list_display_links = ('name',)
    list_filter = ('name', 'phone_number', 'сity', 'new_offer', 'viewed', 'your_list', 'added')
    list_editable = ('new_offer', 'viewed', 'your_list')
    fieldsets = (
        (None, {
            'fields': (('name', 'phone_number', 'сity'),)
        }),
        ('Время звонка', {
            'fields': (('time_to_call_1', 'time_to_call_2'),)
        }),
        ('Дата', {
            'fields': (('date_of_photography',),)
        }),
        ('Фотосъёмка', {
            'fields': (('photography', 'comment'),)
        }),
        ('Показ, фильтры', {
            'fields': (('new_offer', 'viewed', 'your_list'),)
        }),
        ('Заказ сделан', {
            'fields': (('added',),)
        }),

    )
