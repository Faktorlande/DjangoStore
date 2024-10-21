from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request: HttpRequest) -> HttpResponse: #request - экземпляр класса http.request который содержит в себе данные о запросе
    context = {
        'title': 'Home page',
        'content': 'This is the content of the page',
        'list': ['first', 'second'],
        'dict': {'key': 1},
        'is_authenticated': False
    }
    return render(request, template_name='main/index.html', context=context)

def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('About page')
