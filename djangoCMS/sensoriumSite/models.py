from django.db import models
from cms.models.fields import PlaceholderField
from cms.models import CMSPlugin

class TestPlugin(CMSPlugin):
    text=models.CharField(max_length=200)
    def __str__(self):
        return self.text

def slot_siteDescription(instance):
    return 'Description'

	
class myMainModel(models.Model):
    # your fields
    title=models.CharField('title', max_length=255),
    description=models.CharField('description', max_length=255)
    text=models.CharField('text',max_length=200)
	
    my_placeholder = PlaceholderField(slot_siteDescription)

	
	
