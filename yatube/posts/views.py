# from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страницы')


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse(f'Список постов {slug}')
