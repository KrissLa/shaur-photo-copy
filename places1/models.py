from django.db import models
from stdimage import StdImageField


def generate_photoname_pl(instance, filename):
    url = 'Места/%s/%s/%s' % (instance.sity, instance.title, filename)
    return url


class Place(models.Model):
    """Модель места"""
    sity = models.CharField('Город', max_length=50)
    title = models.CharField('Как назвать место?', max_length=100)
    description = models.CharField('Короткое описание', max_length=150)
    user_name = models.CharField('Имя пользователя', max_length=40, blank=True)
    url_map = models.CharField('Ссылка на карте', max_length=300)
    photo = StdImageField('Фотография места', upload_to=generate_photoname_pl,
                                 variations={
                                     'medium': (800, 534),
                                     'small': (100, 67),
                                 }, delete_orphans=True)
    published = models.BooleanField('Опубликовать?', default=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Seo_places(models.Model):
    """SEO"""
    SEO_title = models.CharField('SEO title страницы со списком мест', max_length=70, blank=True,
                                 default=' | Фотограф Светлана Гавриловец | SHAUR-PHOTO.COM | 2020')
    SEO_description = models.CharField('SEO description страницы со списком мест', max_length=150, blank=True)

    def __str__(self):
        return f'title и description страницы со списком мест'

    class Meta:
        verbose_name = 'SEO title и description страницы со списком мест'
        verbose_name_plural = 'SEO title и description страницы со списком мест'
