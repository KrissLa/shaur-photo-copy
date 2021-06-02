from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    """Отзыв"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rev_author')
    created = models.DateTimeField('Дата добавдения', auto_now_add=True, auto_now=False)
    review_body = models.TextField('Отзыв')
    published = models.BooleanField('Опубликовать?', default=True)
    to_main = models.BooleanField('Отобразить на главной', default=False)
    updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'{self.author.first_name} {self.author.last_name}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-created', )


class Seo_reviews(models.Model):
    """SEO"""
    SEO_title = models.CharField('SEO title страницы со списком отзывов', max_length=70, blank=True,
                                 default=' | Фотограф Светлана Гавриловец | SHAUR-PHOTO.COM | 2020')
    SEO_description = models.CharField('SEO description страницы со списком отзывов', max_length=150, blank=True)

    def __str__(self):
        return f'title и description страницы со списком отзывов'

    class Meta:
        verbose_name = 'SEO title и description страницы со списком отзывов'
        verbose_name_plural = 'SEO title и description страницы со списком отзывов'
