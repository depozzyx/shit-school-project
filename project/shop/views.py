# pylint: disable=no-member

from django.http import HttpResponse, HttpRequest
from django.template import loader

from . import models


def index(req: HttpRequest):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("shop/index.html")

    categories = list(models.Category.objects.all().values())
    context = {
        "categories": categories,
    }
    return HttpResponse(template.render(context, req))


def category(req: HttpRequest, category_id: int):
    template = loader.get_template("shop/category.html")

    products = list(models.Product.objects.filter(category=category_id).values())
    category_obj = models.Category.objects.get(id=category_id)
    print(category_obj)
    context = {
        "category": category_obj,
        "products": products,
    }
    return HttpResponse(template.render(context, req))


def order(req: HttpRequest, product_id: int):
    template = loader.get_template("shop/order.html")

    product_obj = models.Product.objects.get(id=product_id)
    context = {
        "product": product_obj,
    }
    return HttpResponse(template.render(context, req))
