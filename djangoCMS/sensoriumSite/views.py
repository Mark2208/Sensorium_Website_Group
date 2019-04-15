# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render

from sensoriumSite.models import myMainModel , aboutUsModel

def index(request):
    
    obj = get_object_or_404(myMainModel)
    return render(request, "site_template/index.html", {'obj': obj,})
	
def about_us(request):
    
    obj = get_object_or_404(aboutUsModel)
    return render(request, "site_template/aboutus.html", {'obj': obj,})
	
def projects(request):
    
    obj = get_object_or_404(myMainModel)
    return render(request, "site_template/projects.html", {'obj': obj,})

def test(request):
    obj = get_object_or_404(myMainModel)

    return render(request, "transitive/index.html", {'obj': obj,})
	