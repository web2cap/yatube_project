from django.shortcuts import render


def index(request):
    """Главная страница."""
    template = "posts/index.html"
    context = {
        "text": "Это главная страница проекта Yatube",
    }
    return render(request, template, context)


def group_posts(request, slug):
    """Страница список постов."""
    template = "posts/group_list.html"
    context = {
        "text": "Здесь будет информация о группах проекта Yatube",
    }
    return render(request, template, context)
