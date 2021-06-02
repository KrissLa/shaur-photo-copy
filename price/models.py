from django.db import models
from django.urls import reverse
from stdimage import StdImageField


# Create your models here.
def generate_photoname_pr(instance, filename):
    url = 'прайс/%s/%s' % (instance.name, filename)
    return url


class Price(models.Model):
    """Модель цен"""
    name = models.CharField('Название фотосъёмки', max_length=150)
    image = StdImageField('Обложка', upload_to=generate_photoname_pr,
                          variations={
                              'medium': (400, 267),
                              'small': (100, 67),
                          }, delete_orphans=True)
    image_alt = models.CharField('SEO alt для обложки', max_length=50, blank=True)
    image_title = models.CharField('SEO title для обложки', max_length=70, blank=True)
    url = models.SlugField('URL', max_length=50, unique=True)
    SEO_title = models.CharField('SEO title', max_length=70, blank=True,
                                 default=' | Фотограф Светлана Гавриловец | SHAUR-PHOTO.COM | 2020')
    SEO_description = models.CharField('SEO description', max_length=150, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('price_detail', kwargs={"slug": self.url})

    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайс'


class Tariff(models.Model):
    """Тарифы"""
    name = models.CharField('Название тарифа', max_length=150)
    price = models.ForeignKey(Price, verbose_name='Название фотосъёмки', on_delete=models.CASCADE, null=True,
                              default='')
    price_sum = models.CharField('Стоимость', max_length=10)

    def __str__(self):
        return self.name

    def get_tariff_li(self):
        return self.tariff_li_set.all().order_by('id')

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'
        ordering = ('id',)


class Tariff_li(models.Model):
    """Пункт списка в тарифе"""
    paragraph = models.CharField('Пункт тарифа', max_length=150)
    tariff = models.ForeignKey(Tariff, verbose_name='тариф', on_delete=models.CASCADE,
                               default='')

    def __str__(self):
        return ''

    class Meta:
        verbose_name = 'Пункт тарифа'
        verbose_name_plural = 'Пункты тарифа'


class Seo_price(models.Model):
    """SEO"""
    SEO_title = models.CharField('SEO title страницы со списком цен', max_length=70, blank=True,
                                 default=' | Фотограф Светлана Гавриловец | SHAUR-PHOTO.COM | 2020')
    SEO_description = models.CharField('SEO description страницы со списком цен', max_length=150, blank=True)

    def __str__(self):
        return f'title и description страницы со списком цен'

    class Meta:
        verbose_name = 'SEO title и description страницы со списком цен'
        verbose_name_plural = 'SEO title и description страницы со списком цен'
