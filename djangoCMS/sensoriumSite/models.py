from django.db import models
from cms.models.fields import PlaceholderField
from cms.models import CMSPlugin

from sensoriumSite.placeholderModels.home_placeholders import home_descriptionModel
from sensoriumSite.placeholderModels.equipment_placeholders import equipment_descriptionModel
from sensoriumSite.placeholderModels.aboutUs_placeholders import aboutUs_descriptionModel



def bioName(instance):
    return 'testName'

		
class Sensorium_Bio(CMSPlugin):
   
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    img_name = models.CharField(max_length=1000)
	
    Twitter_link = models.CharField(max_length=500)
    Facebook_link = models.CharField(max_length=500)
    Linkedin_link = models.CharField(max_length=500)
	
	
    plc_description = PlaceholderField(bioName)
    def __str__(self):              # Python 3: def __unicode__(self):
        return self.name
		
class Sensorium_News(CMSPlugin):
   
    Title = models.CharField(max_length=200)
    Content = models.CharField(max_length=500)
    Sub_content = models.CharField(max_length=1000)
    Image_Source = models.CharField(max_length=5000)
	
 
    plc_news = PlaceholderField('News/Events')
    def __str__(self):              # Python 3: def __unicode__(self):
        return self.Title
		

class Sensorium_Project(CMSPlugin):
   
    Title = models.CharField(max_length=200)
    Content = models.CharField(max_length=500)
    Sub_content = models.CharField(max_length=1000)
    Image_Source = models.CharField(max_length=5000)
	
    def __str__(self):              # Python 3: def __unicode__(self):
        return self.Title
		
		
class image_Backs(CMSPlugin):
   
    homeBack = models.CharField(max_length=5000)
    contentBack = models.CharField(max_length=5000)
    equipmentBack = models.CharField(max_length=5000)
    newsBack = models.CharField(max_length=5000)
	
    def __str__(self):              # Python 3: def __unicode__(self):
        return self.homeBack

		

	

	
   
	
