from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from women.models import Women, Category

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_article'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


def index(request):
    context = {
        'menu': menu,
    }
    return render(request, 'women/index.html', context=context)


def post_detail(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug, is_published=True)
    context = {
        'post': post,
    }
    return render(request, 'women/post_detail.html', context=context)


def about(request):
    context = {
        'menu': menu,
    }
    return render(request, 'women/about.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def add_article(request):
    return HttpResponse('add_article')


def contact(request):
    return HttpResponse('contact')


def login(request):
    return HttpResponse('login')


def show_category(request, category_slug):
    posts = Women.objects.filter(category__slug=category_slug)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, 'women/category_detail.html', context=context)
