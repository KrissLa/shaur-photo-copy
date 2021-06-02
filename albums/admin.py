from django.contrib import admin
from django.utils.safestring import mark_safe
from nested_admin.nested import NestedModelAdmin, NestedStackedInline, NestedTabularInline

from .models import Photography, Photo, Albums, AlbumsDiv


# Register your models here.

@admin.register(Photography)
class PhotographyAdmin(admin.ModelAdmin):
    """Регистрация фотосъёмок на странице администратора"""
    list_display = ('id', 'name', 'slug', 'published', 'get_photography_image_min')
    list_display_links = ('name',)
    save_on_top = True
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ('published',)
    fieldsets = (
        (None, {
            'fields': (('name', 'description'), ('slug', 'published',))
        }),
        ('SEO фотосъёмки', {
            'fields': (('seo_title', 'seo_description'),)
        }),
        ('Изображения', {
            'fields': (
                ('image_min', 'get_photography_image_min'), ('image_bg', 'get_photography_image_bg'),
                ('image_bg_tel', 'get_photography_image_bg_tel'))
        }),
        ('SEO', {
            'fields': (('alt_min', 'title_min', 'alt_bg'),)
        }),
        ('SVG', {
            'fields': (('svg_image',),)
        }),

        ('Прайс', {
            'fields': (('a_price',),)
        }),

    )
    readonly_fields = ('get_photography_image_min', 'get_photography_image_bg', 'get_photography_image_bg_tel')

    def get_photography_image_min(self, obj):
        return mark_safe(f'<img src={obj.image_min.admin.url} width="80">')

    get_photography_image_min.short_description = ''

    def get_photography_image_bg(self, obj):
        return mark_safe(f'<img src={obj.image_bg.admin.url} width="80">')

    get_photography_image_bg.short_description = ''

    def get_photography_image_bg_tel(self, obj):
        return mark_safe(f'<img src={obj.image_bg_tel.admin.url} width="80">')

    get_photography_image_bg_tel.short_description = ''


class PhotoAdmin(NestedTabularInline):
    """Добавление фото на странице администратора на странице альбома"""
    model = Photo
    extra = 4
    readonly_fields = ('get_photo',)
    fieldsets = (
        ('Настройка шаблона', {
            'fields': (('photo', 'get_photo', 'to_index', 'published'),
                       ('alt_photo', 'title_photo'))
        }),
    )

    def get_photo(self, obj):
        return mark_safe(f'<img src={obj.photo.admin.url} width="80">')

    get_photo.short_description = ''

class AlbumsDivAdmin(NestedStackedInline):
    """Добавление контейнеров с фото в админке"""
    model = AlbumsDiv
    extra = 1
    save_on_top = True
    inlines = [PhotoAdmin, ]

@admin.register(Albums)
class AlbumsAdmin(NestedModelAdmin):
    """Добавление альбома на странице администратора"""
    list_display = ('name', 'publish', 'published', 'get_image')
    list_filter = ('photography', 'publish')
    search_fields = ('name',)
    save_on_top = True
    list_editable = ('published',)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [AlbumsDivAdmin, ]
    fieldsets = (
        ('SEO альбома', {
            'fields': (('SEO_title', 'SEO_description'),)
        }),
        ('Альбом', {
            'fields': (('name', 'slug', 'photography'), ('published', 'publish', 'album_to_index'),)
        }),
        ('Изображение', {
            'fields': (('poster', 'get_image', 'alt_poster', 'title_poster'),)
        }),
    )
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.admin.url} width="80">')

    get_image.short_description = ''
