from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from women.models import Women, Category

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_article'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


def index(request):
    posts = Women.objects.filter(is_published=True)
    category = Category.objects.all()
    context = {
        'menu': menu,
        'posts': posts,
        'category': category,
    }
    return render(request, 'women/index.html', context=context)


def post_detail(request, post_id):
    post = Women.objects.get(pk=post_id, is_published=True)
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


def show_category(request, category_id):
    posts = Women.objects.filter(category_id=category_id)
    context = {
        'posts': posts
    }
    return render(request, 'women/category_detail.html', context=context)
