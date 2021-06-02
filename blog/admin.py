from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Post, Seo_blog

# Register your models here.

class PostAdminForm(forms.ModelForm):
    """Регистрация поля ckeditor на сайте администратора"""
    post_body = forms.CharField(label='Статья', widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Статья на сайте администратора"""
    form = PostAdminForm
    list_display = ('id', 'name', 'published', 'get_small_image')
    list_display_links = ('id', 'name')
    save_on_top = True
    list_editable = ('published',)
    prepopulated_fields = {"url": ("name",)}
    list_filter = ('published',)
    search_fields = ('name',)
    readonly_fields = ('get_small_image', 'get_image')
    fieldsets = (
        (None, {
            'fields': (('name', 'url', 'published',),)
        }),
        (None, {
            'fields': (('short_description',),)
        }),
        ('Изображения', {
            'fields': (('small_image', 'get_small_image', 'small_image_alt', 'small_image_title'),
                       ('image', 'get_image'))
        }),
        ('SEO страницы', {
            'fields': (('SEO_title', 'SEO_description'),)
        }),
        ('Статья', {
            'fields': (('post_body',),)
        })
    )

    def get_small_image(self, obj):
        return mark_safe(f'<img src={obj.small_image.small.url} width="80">')

    get_small_image.short_description = ''


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80">')

    get_image.short_description = ''




@admin.register(Seo_blog)
class SeoAdmin(admin.ModelAdmin):
    """SEO страницы БЛОГ"""
    model = Seo_blog