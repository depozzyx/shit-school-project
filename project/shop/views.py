# from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.template import loader


def index(req: HttpRequest):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("shop/index.html")
    context = {
        "categories": ["djdidjd", "kkkk"],
    }
    return HttpResponse(template.render(context, req))
