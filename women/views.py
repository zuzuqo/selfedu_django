from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('Hello')


def categories(request, cat_id):
    return HttpResponse(f'Categories: {cat_id}')


def archive(request, year):
    if int(year) > 2022:
        raise Http404()
        # return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
