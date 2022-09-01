from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from women.models import Women

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):
    posts = Women.objects.all()
    context = {}
    context['menu'] = menu
    context['posts'] = posts
    return render(request, 'women/index.html', context)


def about(request):
    return render(request, 'women/about.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
