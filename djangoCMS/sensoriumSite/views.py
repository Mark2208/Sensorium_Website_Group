# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render
from django.views import generic


from sensoriumSite.placeholderModels.home_placeholders import home_descriptionModel
from sensoriumSite.placeholderModels.equipment_placeholders import equipment_descriptionModel
from sensoriumSite.placeholderModels.aboutUs_placeholders import *

from sensoriumSite.models import Sensorium_Bio


def index(request):
    
    obj = get_object_or_404(home_descriptionModel)
    return render(request, "site_template/index.html", {'obj': obj,})
    
def about_us(request):
    
    obj = get_object_or_404(aboutUs_descriptionModel)
    bio = get_object_or_404(aboutUs_BioPlaceholderModel)
    bio2 = get_object_or_404(aboutUs_BioPlaceholderModel2)
    bio3 = get_object_or_404(aboutUs_BioPlaceholderModel3)
    bio4 = get_object_or_404(aboutUs_BioPlaceholderModel4)
    
    
    return render(request, "site_template/aboutus.html", {
                                                           'obj': obj, 
                                                           'bio': bio,
                                                           'bio2': bio2,
														   'bio3': bio3,
														   'bio4': bio4,
                                                           })
    
def projects(request):
    
    obj = get_object_or_404(home_descriptionModel)
    return render(request, "site_template/projects.html", {'obj': obj,})
    
def equipment(request):
    
    obj = get_object_or_404(equipment_descriptionModel)
    return render(request, "site_template/equipment.html", {'obj': obj,})
	
def newsEvents(request):

    obj = get_object_or_404(news_eventsPlaceholderModel)
    return render(request, "site_template/newsevents.html", {'obj': obj,})

