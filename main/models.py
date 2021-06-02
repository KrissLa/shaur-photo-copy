from django.db import models
from stdimage import StdImageField

# Create your models here.

OBJECT_POSITION_CHOISE = (
    ('bottom', 'Низ'),
    ('center', 'Центр'),
    ('top', 'Верх'),

)


class Main(models.Model):
    """Главная страница"""
    hello = models.CharField('Приветствие', max_length=200)
    about_body = models.TextField('Обо мне')
    about_photo = StdImageField('Фотография в "обо мне"', upload_to='main', null=True, blank=True,
                                variations={
                                    'small': (80, 80),
                                }, delete_orphans=True
                                )
    about_background = StdImageField('Фотография фона в "обо мне"', upload_to='main', null=True, blank=True,
                                     variations={
                                         'small': (100, 67),
                                     }, delete_orphans=True)
    about_background_object_position = models.CharField('Позиция фотографии фона блока "Обо мне"',
                                                        choices=OBJECT_POSITION_CHOISE, max_length=10, blank=True,
                                                        null=True)
    about_background_tel = StdImageField('Фотография фона для телефонов в "обо мне"', upload_to='main', null=True,
                                         blank=True,
                                         variations={
                                             'small': (100, 67),
                                         }, delete_orphans=True)
    reviews_background = StdImageField('Фотография фона в блоке "отзывы"', upload_to='main', null=True, blank=True,
                                       variations={
                                           'small': (100, 67),
                                       }, delete_orphans=True)
    blog_background = StdImageField('Фотография фона в блоке "блог"', upload_to='main', null=True, blank=True,
                                    variations={
                                        'small': (100, 67),
                                    }, delete_orphans=True)
    image_pl1 = StdImageField('Первая картинка в секции места', upload_to='main', variations={
        'small': (100, 67),
    }, delete_orphans=True)
    image_pl2 = StdImageField('Вторая картинка в секции места', upload_to='main', variations={
        'small': (100, 67),
    }, delete_orphans=True)
    image_pl1_alt = models.CharField('SEO alt для первой картинки', max_length=50, blank=True)
    image_pl2_alt = models.CharField('SEO alt для второй картинки', max_length=50, blank=True)
    image_pl_title = models.CharField('SEO title для картинок', max_length=70, blank=True)
    SEO_title = models.CharField('SEO title главной страницы', max_length=70, blank=True,
                                 default=' | Фотограф Светлана Гавриловец | SHAUR-PHOTO.COM | 2020')
    SEO_description = models.CharField('SEO description главной страницы', max_length=150, blank=True)
    about = models.BooleanField('Включить блок "Обо мне"', default=False)
    last_album = models.BooleanField('Включить блок "Последний альбом"', default=False)
    photography = models.BooleanField('Включить блок "Фотосъёмки"', default=False)
    reviews = models.BooleanField('Включить блок "Отзывы"', default=False)
    blog = models.BooleanField('Включить блок "Блог"', default=False)
    place = models.BooleanField('Включить блок "Места"', default=False)
    offer_ph = models.BooleanField('Включить форму заказа', default=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Главная'

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'
