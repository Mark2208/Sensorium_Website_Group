from django.db import models
from cms.models.fields import PlaceholderField
from cms.models import CMSPlugin

def slot_Description(instance):
    return 'Description'

def slot_Bio(instance):
    return 'User Group'
	

class news_eventsPlaceholderModel(models.Model):
    # your fields
    plc_news = PlaceholderField("News/Events")
	
class aboutUs_descriptionModel(models.Model):
    # your fields
    plc_description = PlaceholderField("Main Description")
	
class aboutUs_BioPlaceholderModel(models.Model):
    # your fields
    plc_bio = PlaceholderField("Bio Line")
	
class aboutUs_BioPlaceholderModel2(models.Model):
    # your fields
    plc_bio = PlaceholderField("Bio Line")
	
class aboutUs_BioPlaceholderModel3(models.Model):
# your fields
    plc_bio = PlaceholderField("Bio Line")

class aboutUs_BioPlaceholderModel4(models.Model):
# your fields
    plc_bio = PlaceholderField("Bio Line")
	

	
	
	
	
	