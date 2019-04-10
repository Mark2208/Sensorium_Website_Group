# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render


def index(request):
    #template = loader.get_template("sidebar_left.html")
    return HttpResponse("Hello world")

def testPage(request):
    return render(request, "transitive/index.html", {})
