# from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, HttpRequest


def index(req: HttpRequest):
    return HttpResponse("Hello, world. You're at the polls index.")
