from django.db import models
from cms.models.fields import PlaceholderField
from cms.models import CMSPlugin

def slot_description(instance):
    return 'Description'
	
	
class home_descriptionModel(models.Model):
    # your fields
    plc_description = PlaceholderField(slot_description)