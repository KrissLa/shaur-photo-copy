from django.db import models
from django.urls import reverse
from stdimage import StdImageField


# Create your models here.
def generate_photoname_blog(instance, filename):
    url = 'блог/%s/миниатюра/%s' % (instance.name, filename)
    return url


def generate_photoname_blog_bg(instance, filename):
    url = 'блог/%s/большая/%s' % (instance.name, filename)
    return url


class Post(models.Model):
    """Модель поста блога"""
    name = models.CharField('Название статьи', max_length=100)
    url = models.SlugField('URL', max_length=50, unique=True)
    short_description = models.CharField('Краткое описание', max_length=200)
    small_image = StdImageField('Миниатюра для статьи',
                                  upload_to=generate_photoname_blog,
                                  variations={
                                      'medium': (500, 334),
                                      'small': (100, 67),
                                  }, delete_orphans=True)
    small_image_alt = models.CharField('SEO alt для миниатюры', max_length=50, blank=True)
    small_image_title = models.CharField('SEO title для миниатюры', max_length=70, blank=True)
    image = models.ImageField('Картинка в самой статье (большой размер)', upload_to=generate_photoname_blog_bg)
    post_body = models.TextField('Статья',)
    SEO_title = models.CharField('SEO title', max_length=70, blank=True,
                                 default=' | Фотограф Светлана Гавриловец | SHAUR-PHOTO.COM | 2020')
    SEO_description = models.CharField('SEO description', max_length=150, blank=True)
    published = models.BooleanField('Опубликовать?', default=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug": self.url})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-id',)



class Seo_blog(models.Model):
    """SEO"""
    SEO_title = models.CharField('SEO title страницы со списком статей', max_length=70, blank=True,
                                 default=' | Фотограф Светлана Гавриловец | SHAUR-PHOTO.COM | 2020')
    SEO_description = models.CharField('SEO description страницы со списком статей', max_length=150, blank=True)

    def __str__(self):
        return f'title и description страницы со списком статей'

    class Meta:
        verbose_name = 'SEO title и description страницы со списком статей'
        verbose_name_plural = 'SEO title и description страницы со списком статей'
