from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Main
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


# Register your models here.

class MainAdminForm(forms.ModelForm):
    """Добавление поля ckeditor"""
    about_body = forms.CharField(label='Обо мне', widget=CKEditorUploadingWidget())

    class Meta:
        model = Main
        fields = '__all__'


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    """Регистрация главной страницы на сайте администратора"""
    model = Main
    form = MainAdminForm
    save_on_top = True
    list_display = ('__str__', 'about', 'last_album', 'photography', 'reviews', 'blog', 'place', 'offer_ph')
    list_editable = ('about', 'last_album', 'photography', 'reviews', 'blog', 'place', 'offer_ph')
    readonly_fields = (
        'get_image_pl1', 'get_image_pl2', 'get_about_photo', 'get_about_background', 'get_reviews_background',
        'get_about_background_tel', 'get_blog_background')
    fieldsets = (
        ('SEO страницы', {
            'fields': (('SEO_title', 'SEO_description'),)
        }),
        ('Обо мне', {
            'fields': (('hello',),
                       ('about_body',),
                       ('about_photo', 'get_about_photo',),
                       ('about_background', 'get_about_background', 'about_background_object_position'),
                       ('about_background_tel', 'get_about_background_tel'))
        }),
        ('Отзывы', {
            'fields': (('reviews_background', 'get_reviews_background'),)
        }),
        ('Блог', {
            'fields': (('blog_background', 'get_blog_background'),)
        }),
        ('Места (картинки 512х512 или больше. Соотношение сторон 1:1) ', {
            'fields': (('image_pl1', 'get_image_pl1', 'image_pl1_alt'),
                       ('image_pl2', 'get_image_pl2', 'image_pl2_alt', 'image_pl_title'),)
        }),
        ('Блоки', {
            'fields': (('about', 'last_album', 'photography', 'reviews', 'blog', 'place', 'offer_ph'),)
        }),
    )

    def get_image_pl1(self, obj):
        return mark_safe(f'<img src={obj.image_pl1.small.url} width="80">')

    get_image_pl1.short_description = ''

    def get_image_pl2(self, obj):
        return mark_safe(f'<img src={obj.image_pl2.small.url} width="80">')

    get_image_pl2.short_description = ''

    def get_about_photo(self, obj):
        return mark_safe(f'<img src={obj.about_photo.small.url} width="80">')

    get_about_photo.short_description = ''

    def get_about_background(self, obj):
        return mark_safe(f'<img src={obj.about_background.small.url} width="80">')

    get_about_background.short_description = ''

    def get_reviews_background(self, obj):
        return mark_safe(f'<img src={obj.reviews_background.small.url} width="80">')

    get_reviews_background.short_description = ''

    def get_about_background_tel(self, obj):
        return mark_safe(f'<img src={obj.reviews_background_tel.small.url} width="80">')

    get_about_background_tel.short_description = ''

    def get_blog_background(self, obj):
        return mark_safe(f'<img src={obj.blog_background.small.url} width="80">')

    get_blog_background.short_description = ''
