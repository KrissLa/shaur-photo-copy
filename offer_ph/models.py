from django.db import models
from django.utils import timezone


# Create your models here.

class Offer(models.Model):
    """Как заказать фотосъёмку"""
    SEO_title = models.CharField('SEO title', max_length=70, blank=True,
                                 default=' | Фотограф Светлана Гавриловец | SHAUR-PHOTO.COM | 2020')
    SEO_description = models.CharField('SEO description', max_length=150, blank=True)
    body = models.TextField('Как заказать фотосъёмку')
    published = models.BooleanField('Опубликовать', default=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = 'Инструкция заказа фотосъёмки'
        verbose_name_plural = 'Инструкции заказа фотосъёмки'


class Offer_li(models.Model):
    """Пункты списка с ссылками"""
    anchor = models.CharField('Текст ссылки', max_length=200)
    a_soc_net = models.CharField('Cсылка на соц сеть для ПК', max_length=150)
    a_soc_net_tel = models.CharField('Cсылка на соц сеть для ТЕЛЕФОНОВ', max_length=150, default='')
    offer = models.ForeignKey(Offer, verbose_name='инструкция', on_delete=models.CASCADE, null=True, default='')

    def __str__(self):
        return self.anchor

    class Meta:
        verbose_name = 'Ссылка на соц сеть'
        verbose_name_plural = 'Ссылка на соц сети'


class OfferPhotography(models.Model):
    """Модель заказа фотосъёмки"""

    TIME_TO_CALL = (
        ('с 09:00', 'с 09:00'),
        ('с 08:00', 'с 08:00'),
        ('с 10:00', 'с 10:00'),
        ('с 11:00', 'с 11:00'),
        ('с 12:00', 'с 12:00'),
        ('с 13:00', 'с 13:00'),
        ('с 14:00', 'с 14:00'),
        ('с 15:00', 'с 15:00'),
        ('с 16:00', 'с 16:00'),
        ('с 17:00', 'с 17:00'),
        ('с 18:00', 'с 18:00'),
        ('с 19:00', 'с 19:00'),
        ('с 20:00', 'с 20:00'),
        ('с 21:00', 'с 21:00'),

    )
    TIME_TO_CALL_2 = (
        ('до 09:00', 'до 09:00'),
        ('до 10:00', 'до 10:00'),
        ('до 11:00', 'до 11:00'),
        ('до 12:00', 'до 12:00'),
        ('до 13:00', 'до 13:00'),
        ('до 14:00', 'до 14:00'),
        ('до 15:00', 'до 15:00'),
        ('до 16:00', 'до 16:00'),
        ('до 17:00', 'до 17:00'),
        ('до 18:00', 'до 18:00'),
        ('до 19:00', 'до 19:00'),
        ('до 20:00', 'до 20:00'),
        ('до 21:00', 'до 21:00'),
        ('до 22:00', 'до 22:00'),
    )

    PHOTOGRAPHY_CHOISE = (
        ('Свадебная фотосъёмка', 'Свадебная фотосъёмка'),
        ('Love Story', 'Love Story'),
        ('Семейная фотосъёмка', 'Семейная фотосъёмка'),
        ('Детская фотосъёмка', 'Детская фотосъёмка'),
        ('Индивидуальная фотосъёмка', 'Индивидуальная фотосъёмка'),
        ('День рождения', 'День рождения'),
        ('Новогодняя фотосъёмка', 'Новогодняя фотосъёмка'),
        ('Другая фотосъёмка', 'Другая фотосъёмка'),

    )

    name = models.CharField('Имя клиента', max_length=200)
    phone_number = models.CharField('Номер телефона', max_length=13)
    time_to_call_1 = models.CharField(choices=TIME_TO_CALL, max_length=10)
    time_to_call_2 = models.CharField(choices=TIME_TO_CALL_2, max_length=10)
    date_of_photography = models.CharField('Дата', max_length=300)
    photography = models.CharField('Вид фотосъёмки', choices=PHOTOGRAPHY_CHOISE, max_length=30)
    сity = models.CharField('Город', max_length=50)
    comment = models.TextField('Комментарий', max_length=5000, blank=True)
    new_offer = models.BooleanField('Новый заказ', default=True)
    viewed = models.BooleanField('Просмотрено', default=False)
    your_list = models.BooleanField('Отдельний список', default=False)
    added = models.DateTimeField('Заказ сделан', default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
