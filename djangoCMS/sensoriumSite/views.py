# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render

from sensoriumSite.models import myMainModel

def index(request):
    
    #obj = get_object_or_404(myMainModel)
    #obj = myMainModel.objects.first()
    obj = get_object_or_404(myMainModel)

    return render(request, "transitive/index.html", {'obj': obj,})

def test(request):
    return render(request, "transitive/index.html", {})
	