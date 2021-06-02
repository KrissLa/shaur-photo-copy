from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, Seo_places

# Register your models here.


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    """Регистрация места на сайте администратора"""
    model = Place
    save_on_top = True
    readonly_fields = ('get_image',)
    list_display = ('id', 'title', 'sity', 'user_name', 'get_image', 'published')
    list_display_links = ('title',)
    list_filter = ('user_name', 'published', 'sity')
    list_editable = ('published',)
    fieldsets = (
        (None, {
            'fields': (('title', 'sity', 'published'),)
        }),
        (None, {
            'fields': (('description', 'url_map'),)
        }),
        (None, {
            'fields': (('user_name',),)
        }),
        ('Изображение', {
            'fields': (('photo', 'get_image',),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.small.url} width="80">')

    get_image.short_description = ''



@admin.register(Seo_places)
class Seo_placesAdmin(admin.ModelAdmin):
    """SEO на сайте администратора"""
    model = Seo_places