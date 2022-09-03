from django import template
from women.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('women/tag/category_list.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        categories = Category.objects.all()
    else:
        categories = Category.objects.order_by(sort)

    return {'categories': categories, 'cat_selected': cat_selected}


@register.inclusion_tag('women/tag/post_list.html')
def show_posts(sort=None):
    if not sort:
        posts = Women.objects.filter(is_published=True)
    else:
        posts = Women.objects.filter(is_published=True).order_by(sort)
    return {'posts': posts}
