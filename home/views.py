from django.shortcuts import render
from django.template import RequestContext

def index(request):
    return render(request, "home/index.html")


def page_not_found(request, exception):
    return render(request, "home/error/404.html")
    