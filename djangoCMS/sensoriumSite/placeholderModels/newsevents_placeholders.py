from django.db import models
from cms.models.fields import PlaceholderField
from cms.models import CMSPlugin

class news_descriptionPlaceholderModel(models.Model):
# your fields
    plc_description = PlaceholderField("Description")