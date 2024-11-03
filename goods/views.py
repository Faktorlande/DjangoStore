from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from goods.models import Products


def catalog(request, category_slug=False) -> HttpResponse:

    if category_slug == "all":
        goods = Products.objects.all()

    else:
        goods = get_object_or_404(Products.objects.filter(category__slug=category_slug))

    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }

    return render(request, template_name="goods/catalog.html", context=context)


def product(request, product_slug) -> HttpResponse:

    product = Products.objects.get(slug=product_slug)

    context = {
        "product": product,
    }

    return render(request, template_name="goods/product.html", context=context)
