from django.db import models
from cms.models.fields import PlaceholderField
from cms.models import CMSPlugin

class TestPlugin(CMSPlugin):
    text=models.CharField(max_length=200)
    def __str__(self):
        return self.text

def slot_siteDescription(instance):
    return 'Description'
	

def slot_aboutUsDescription(instance):
    return 'Description'

	
class myMainModel(models.Model):
    # your fields
    plc_description = PlaceholderField(slot_siteDescription)
	
class aboutUsModel(models.Model):
    # your fields
    plc_about_us = PlaceholderField(slot_aboutUsDescription)
	
	
   
	
