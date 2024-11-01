from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from goods.models import Products


def catalog(request) -> HttpResponse:

    goods = Products.objects.all()

    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }

    return render(request, template_name="goods/catalog.html", context=context)


def product(request) -> HttpResponse:

    return render(request, template_name="goods/product.html")
