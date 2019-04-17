from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin

from sensoriumSite.placeholderModels.home_placeholders import home_descriptionModel
from sensoriumSite.placeholderModels.equipment_placeholders import equipment_descriptionModel
from sensoriumSite.placeholderModels.aboutUs_placeholders import aboutUs_descriptionModel

	
class myModelAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(home_descriptionModel, myModelAdmin)
admin.site.register(aboutUs_descriptionModel, myModelAdmin)
admin.site.register(equipment_descriptionModel, myModelAdmin)