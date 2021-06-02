from django.contrib import admin
from nested_admin.nested import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from django.utils.safestring import mark_safe

from .models import Price, Tariff, Tariff_li, Seo_price


# Register your models here.
@admin.register(Seo_price)
class Seo_priceAdmin(admin.ModelAdmin):
    """SEO страницы ПРАЙС"""
    model = Seo_price


class Tariff_liAdmin(NestedTabularInline):
    """Добавление пунктов тарифа на странице прайс"""
    model = Tariff_li
    extra = 3



class TariffAdmin(NestedStackedInline):
    """Добавление тарифа на странице прайс"""
    model = Tariff
    extra = 2
    save_on_top = True
    inlines = [Tariff_liAdmin, ]


@admin.register(Price)
class PriceAdmin(NestedModelAdmin):
    """Прайс в админке"""
    list_display = ('id', 'name', 'url', 'get_image')
    list_display_links = ('name',)
    save_on_top = True
    inlines = [TariffAdmin, ]
    prepopulated_fields = {"url": ("name",)}
    readonly_fields = ('get_image', )
    fieldsets = (
        ('SEO альбома', {
            'fields': (('SEO_title', 'SEO_description'),)
        }),
        ('Прайс', {
            'fields': (('name', 'url'),)
        }),
        ('Изображение', {
            'fields': (('image', 'get_image', 'image_alt', 'image_title'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.small.url} width="80">')

    get_image.short_description = ''
