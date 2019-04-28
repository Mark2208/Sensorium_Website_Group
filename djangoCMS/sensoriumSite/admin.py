from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin

from sensoriumSite.placeholderModels.home_placeholders import home_descriptionModel
from sensoriumSite.placeholderModels.equipment_placeholders import equipment_descriptionModel
from sensoriumSite.placeholderModels.aboutUs_placeholders import *
	
class myModelAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(home_descriptionModel, myModelAdmin)

admin.site.register(news_eventsPlaceholderModel, myModelAdmin)

#About_us Placeholders
admin.site.register(aboutUs_descriptionModel, myModelAdmin)
admin.site.register(aboutUs_BioPlaceholderModel, myModelAdmin)
admin.site.register(aboutUs_BioPlaceholderModel2, myModelAdmin)
admin.site.register(aboutUs_BioPlaceholderModel3, myModelAdmin)
admin.site.register(aboutUs_BioPlaceholderModel4, myModelAdmin)



admin.site.register(equipment_descriptionModel, myModelAdmin)

