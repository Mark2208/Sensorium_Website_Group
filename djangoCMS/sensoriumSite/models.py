from django.db import models
from cms.models.fields import PlaceholderField
from cms.models import CMSPlugin

from sensoriumSite.placeholderModels.home_placeholders import home_descriptionModel
from sensoriumSite.placeholderModels.equipment_placeholders import equipment_descriptionModel
from sensoriumSite.placeholderModels.aboutUs_placeholders import aboutUs_descriptionModel

class TestPlugin(CMSPlugin):
    text=models.CharField(max_length=200)
    def __str__(self):
        return self.text


	

	
   
	
