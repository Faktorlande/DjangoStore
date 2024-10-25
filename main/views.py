from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request: HttpRequest) -> HttpResponse: #request - экземпляр класса http.request который содержит в себе данные о запросе
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }
    return render(request, template_name='main/index.html', context=context)

def about(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'About - О нас',
        'content': 'Информация о магазине',
        'about_text': """Магазин мебели HOME\n
                         Это учебный проект. Работаем с шаблонами""",
    }
    return render(request, template_name='main/about.html', context=context)
