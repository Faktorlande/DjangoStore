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


def product(request, product_slug) -> HttpResponse:
    
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product,
    }

    return render(request, template_name="goods/product.html", context=context)
