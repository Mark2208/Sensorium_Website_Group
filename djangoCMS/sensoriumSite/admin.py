from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin

from sensoriumSite.models import image_Backs
from sensoriumSite.placeholderModels.home_placeholders import home_descriptionModel
from sensoriumSite.placeholderModels.equipment_placeholders import equipment_descriptionModel
from sensoriumSite.placeholderModels.aboutUs_placeholders import *
from sensoriumSite.placeholderModels.projects_placeholders import project_PlaceholderModel, project_descriptionPlaceholderModel
from sensoriumSite.placeholderModels.newsevents_placeholders import news_descriptionPlaceholderModel


class myModelAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    frontend_editable_fields = ("foo", "bar")
    pass
	


admin.site.register(home_descriptionModel, myModelAdmin)

#Register the News Placeholder
admin.site.register(news_eventsPlaceholderModel, myModelAdmin)
admin.site.register(news_descriptionPlaceholderModel, myModelAdmin)

#Register the Project Placeholder 
admin.site.register(project_PlaceholderModel, myModelAdmin)
admin.site.register(project_descriptionPlaceholderModel, myModelAdmin)

#Register the Images Model
admin.site.register(image_Backs, myModelAdmin)



#About_us Bio Placeholders
admin.site.register(aboutUs_descriptionModel, myModelAdmin)
admin.site.register(aboutUs_BioPlaceholderModel, myModelAdmin)
admin.site.register(aboutUs_BioPlaceholderModel2, myModelAdmin)
admin.site.register(aboutUs_BioPlaceholderModel3, myModelAdmin)
admin.site.register(aboutUs_BioPlaceholderModel4, myModelAdmin)


#Home Placeholder
admin.site.register(equipment_descriptionModel, myModelAdmin)

