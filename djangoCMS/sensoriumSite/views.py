# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render

from sensoriumSite.placeholderModels.home_placeholders import home_descriptionModel
from sensoriumSite.placeholderModels.equipment_placeholders import equipment_descriptionModel
from sensoriumSite.placeholderModels.aboutUs_placeholders import aboutUs_descriptionModel


def index(request):
    
    obj = get_object_or_404(home_descriptionModel)
    return render(request, "site_template/index.html", {'obj': obj,})
	
def about_us(request):
    
    obj = get_object_or_404(aboutUs_descriptionModel)
    return render(request, "site_template/aboutus.html", {'obj': obj,})
	
def projects(request):
    
    obj = get_object_or_404(home_descriptionModel)
    return render(request, "site_template/projects.html", {'obj': obj,})
	
def equipment(request):
    
    obj = get_object_or_404(equipment_descriptionModel)
    return render(request, "site_template/equipment.html", {'obj': obj,})

