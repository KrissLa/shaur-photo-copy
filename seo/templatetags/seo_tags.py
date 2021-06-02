from django import template
from ..models import CounterForSite, ConnectSSModel

register = template.Library()

@register.inclusion_tag('template_tags/seo_tags.html')
def all_counter(published=True):
    counters = CounterForSite.objects.filter(published=published)
    return {'counters':counters}


@register.inclusion_tag('template_tags/seo_tags.html')
def all_ss(published=True):
    ss = ConnectSSModel.objects.filter(published=published)
    return {'ss':ss}
