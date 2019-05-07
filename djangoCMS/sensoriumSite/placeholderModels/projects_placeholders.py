from django.db import models
from cms.models.fields import PlaceholderField
from cms.models import CMSPlugin

class project_descriptionPlaceholderModel(models.Model):
# your fields
    plc_description = PlaceholderField("Description")
	

class project_PlaceholderModel(models.Model):
# your fields
    plc_project = PlaceholderField("Project")
	

	

	
	
	
	
	