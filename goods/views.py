from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def catalog(request) -> HttpResponse:

    return render(request, template_name='goods/catalog.html')

def product(request) -> HttpResponse:

    return render(request, template_name='goods/product.html')