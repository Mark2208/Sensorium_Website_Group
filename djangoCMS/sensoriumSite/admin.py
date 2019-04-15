from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from sensoriumSite.models import myMainModel, aboutUsModel

	
class myModelAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(myMainModel, myModelAdmin)
admin.site.register(aboutUsModel, myModelAdmin)