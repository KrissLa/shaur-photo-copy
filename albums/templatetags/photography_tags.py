from django import template
from ..models import Photography

register = template.Library()


@register.inclusion_tag('template_tags/photography_tag.html')
def all_photography(published=True):
    """Фотосъёмки для меню"""
    a_p = Photography.objects.filter(published=published).order_by('id')
    return {'a_p': a_p}
