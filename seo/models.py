from django.db import models

# Create your models here.
class ConnectSSModel(models.Model):
    """Модель для подключение ПС"""
    name = models.CharField("Имя", max_length=60, help_text="Имя поисковой системы")
    key = models.CharField("Код", max_length=500)
    published = models.BooleanField("Включен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подключение ПС"
        verbose_name_plural = "Подключение ПС"


class CounterForSite(models.Model):
    """Счечики и аналитика для сайта"""
    name = models.CharField("Имя", max_length=60, help_text="Имя счетчика")
    code = models.TextField("Код", help_text="Код счетчика или метрики")
    published = models.BooleanField("Включен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Счетчики и аналитика для сайта"
        verbose_name_plural = "Счетчики и аналитика для сайта"
