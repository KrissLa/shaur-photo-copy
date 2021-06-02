from datetime import date
from django.utils import timezone
import datetime
from django.db import models
from django.urls import reverse
from stdimage import StdImageField


# Create your models here.
def generate_photoname_ph(instance, filename):
    url = 'фотосъёмки/%s/миниатюра/%s' % (instance.name, filename)
    return url


def generate_photoname_ph_bg(instance, filename):
    url = 'фотосъёмки/%s/фон/%s' % (instance.name, filename)
    return url


def generate_photoname_ph_bg_tel(instance, filename):
    url = 'фотосъёмки/%s/фон_мобилки/%s' % (instance.name, filename)
    return url


class Photography(models.Model):
    """Виды фотосъёмок"""

    name = models.CharField('Название фотосъёмки', max_length=50)
    slug = models.SlugField(max_length=50, unique=True, null=True)
    seo_title = models.CharField('SEO title', max_length=70, blank=True,
                                     default=' | Фотограф Светлана Гавриловец | SHAUR-PHOTO.COM | 2020')
    seo_description = models.CharField('SEO description', max_length=150, blank=True)
    description = models.TextField('Описание фотосъёмки')
    svg_image = models.TextField('Анимированная svg', blank=True)
    image_min = StdImageField('Миниатюра для фотоcъёмки',
                              upload_to=generate_photoname_ph,
                              variations={
                                  'small': (50, 33),
                                  'admin': (80, 53),
                              }, delete_orphans=True)
    alt_min = models.CharField('SEO alt для миниатюры', max_length=50, blank=True)
    title_min = models.CharField('SEO title для миниатюры', max_length=70, blank=True)
    image_bg = StdImageField('Фоновое изображение', upload_to=generate_photoname_ph_bg,
                             variations={
                                 'small': (50, 33),
                                 'admin': (80, 53),
                             }, delete_orphans=True)
    image_bg_tel = StdImageField('Фоновое изображение для мобильных',
                                 upload_to=generate_photoname_ph_bg_tel,
                                 variations={
                                     'small': (50, 33),
                                     'admin': (80, 120),
                                 }, delete_orphans=True)
    alt_bg = models.CharField('SEO alt для фонового изображения', max_length=50, blank=True)
    a_price = models.TextField('Ссылка на прайс', max_length=400, blank=True)
    published = models.BooleanField('Опубликовать?', default=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_albums(self):
        return self.albums_set.filter(published=True)

    def get_absolute_url(self):
        return reverse('albums_list_by_photography', args=[self.slug])

    class Meta:
        verbose_name = 'Фотосъёмка'
        verbose_name_plural = 'Фотосъёмки'
        ordering = ('id',)


def generate_photoname_al(instance, filename):
    url = 'альбомы/%s/%s/обложка/%s' % (instance.photography.name, instance.name, filename)
    return url


class Albums(models.Model):
    """Альбомы"""
    name = models.CharField('Название', max_length=75)
    poster = StdImageField('Обложка альбома', upload_to=generate_photoname_al,
                           variations={
                               'large': (600, 400),
                               'medium': (400, 267),
                               'admin': (80, 53),
                               'small': (50, 33),
                           }, delete_orphans=True)
    alt_poster = models.CharField('SEO alt для обложки', max_length=70, blank=True)
    title_poster = models.CharField('SEO title для обложки', max_length=70, blank=True)
    photography = models.ForeignKey(Photography, verbose_name='Фотосъёмка', on_delete=models.SET_NULL, null=True,
                                    default='')
    slug = models.SlugField('URL', max_length=50, unique=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField('Добавлен', default=timezone.now)
    published = models.BooleanField('Опубликовать?', default=True)
    SEO_title = models.CharField('SEO title', max_length=70, blank=True,
                                 default=' | Фотограф Светлана Гавриловец | SHAUR-PHOTO.COM | 2020')
    SEO_description = models.CharField('SEO description', max_length=150, blank=True)
    album_to_index = models.BooleanField('Выбрать для главной', default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('albums_detail', args=[self.id, self.slug])

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.publish >= now - datetime.timedelta(days=3)

    def was_published(self):
        now = timezone.now()
        return now >= self.publish

    def get_last_albums_photo(self):
        """Получаем выбранные фотографии для отображение на главной"""
        return self.albumsdiv_set.all()

    def get_albums(self):
        return self.albumsdiv_set.photo_set.filter(published=True).order_by('pk')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ('-publish',)
        index_together = (('id', 'slug'),)


def generate_photoname(instance, filename):
    url = 'альбомы/%s/фото/%s/' % (instance.div.album.name, filename)
    return url


class AlbumsDiv(models.Model):
    """Контейнеры для фото"""

    DIV_CLASS_CHOISE = (
        ('a-g-1', 'Большое фото'),
        ('a-g-2', '2 одинаковых фото'),
        ('a-g-2-1', '2 фото: Гор - Вер'),
        ('a-g-1-2', '2 фото: Вер - Гор'),
        ('a-g-3', '3 одинаковых фото'),
        ('a-g-2-1-1', '3 фото: Гор - Вер - Вер'),
        ('a-g-2-2-1', '3 фото: Гор - Гор - Вер'),
        ('a-g-2-1-2', '3 фото: Гор - Вер - Гор'),
        ('a-g-1-2-2', '3 фото: Вер - Гор - Гор'),
        ('a-g-1-1-2', '3 фото: Вер - Вер - Гор'),
        ('a-g-1-2-1', '3 фото: Вер - Гор - Вер'),
        ('a-g-4', '4 одинаковых фото'),
        ('a-g-1-2-2-2', '4 фото: Вер - Гор - Гор - Гор'),
        ('a-g-1-1-2-2', '4 фото: Вер - Вер - Гор - Гор'),
        ('a-g-1-1-1-2', '4 фото: Вер - Вер - Вер - Гор'),
        ('a-g-2-1-1-1', '4 фото: Гор - Вер - Вер - Вер'),
        ('a-g-2-2-1-1', '4 фото: Гор - Гор - Вер - Вер'),
        ('a-g-2-2-2-1', '4 фото: Гор - Гор - Гор - Вер'),
        ('a-g-1-2-1-1', '4 фото: Вер - Гор - Вер - Вер'),
        ('a-g-1-2-2-1', '4 фото: Вер - Гор - Гор - Вер'),
        ('a-g-1-1-2-1', '4 фото: Вер - Вер - Гор - Вер'),
        ('a-g-2-1-2-2', '4 фото: Гор - Вер - Гор - Гор'),
        ('a-g-2-2-1-2', '4 фото: Гор - Гор - Вер - Гор'),
    )

    album = models.ForeignKey(Albums, verbose_name='Альбом', on_delete=models.CASCADE, null=True)
    div_class = models.CharField('Шаблон контейнера', choices=DIV_CLASS_CHOISE, max_length=35)

    def __str__(self):
        return f'{self.div_class}'

    def get_photo(self):
        return self.photo_set.filter(published=True)

    def get_photo_to_main(self):
        return self.photo_set.filter(published=True).filter(to_index=True)

    class Meta:
        verbose_name = 'Контейнер'
        verbose_name_plural = 'Контейнеры'
        ordering = ('pk',)


class Photo(models.Model):
    """Фотографии"""
    photo = StdImageField('Фото',
                          upload_to=generate_photoname,
                          blank=True, variations={
            'ag1': (1329, 1996),
            'ag2': (669, 993),
            'ag21': (917, 612), #a-g-1-2
            'ag3': (439, 659),
            'ag211': (698, 466), #a-g-1-1-2, a-g-1-2-1
            'ag221': (539, 360), #a-g-2-1-2, a-g-1-2-2
            'ag4': (329, 492),
            'ag1222': (381, 254), #a-g-2-2-2-1, a-g-2-1-2-2, a-g-2-2-1-2
            'ag1122': (454, 303), #a-g-2-2-1-1, a-g-1-2-2-1
            'ag1112': (562, 376), #a-g-2-1-1-1, a-g-1-2-1-1, a-g-1-1-2-1
            'admin': (80, 120),
            'small': (50, 75),
        }, delete_orphans=True)
    alt_photo = models.CharField('SEO alt', max_length=70, blank=True)
    title_photo = models.CharField('SEO title', max_length=70, blank=True)
    div = models.ForeignKey(AlbumsDiv, verbose_name='Альбом', on_delete=models.CASCADE, default='', null=True)
    to_index = models.BooleanField('Отобразить на главной (Новый альбом)', default=False)
    published = models.BooleanField('Опубликовать?', default=True)

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'ФОТОГРАФИЯ'
        verbose_name_plural = 'ФОТОГРАФИИ'
        ordering = ('pk',)


def generate_photoname_ver(instance, filename):
    url = 'альбомы/%s/%s/вертикальные/%s/' % (instance.album.photography.name, instance.album.name, filename)
    return url


# class Seo_albums(models.Model):
#     """SEO"""
#     SEO_title = models.CharField('SEO title страницы со списком альбомов', max_length=70, blank=True,
#                                  default=' | Фотограф Светлана Гавриловец | SHAUR-PHOTO.COM | 2020')
#     SEO_description = models.CharField('SEO description страницы со списком альбомов', max_length=150, blank=True)
#
#     def __str__(self):
#         return f'title и description страницы со списком альбомов'
#
#     class Meta:
#         verbose_name = 'SEO title и description страницы со списком альбомов'
#         verbose_name_plural = 'SEO title и description страницы со списком альбомов'
