from django.contrib import admin

from .models import Review, Seo_reviews
# Register your models here.

@admin.register(Seo_reviews)
class SeoAdmin(admin.ModelAdmin):
    """SEO страницы АЛЬБОМЫ"""
    model = Seo_reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы на сайте администратора"""
    model = Review
    list_display = ('__str__', 'created', 'published', 'to_main')
    list_display_links = ('__str__', 'created')
    list_editable = ('published', 'to_main')
    list_filter = ('created', 'published', 'to_main')

    readonly_fields = ('created',)