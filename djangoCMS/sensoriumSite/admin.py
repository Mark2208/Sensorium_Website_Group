from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from sensoriumSite.models import myMainModel

	
class MainModelAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(myMainModel, MainModelAdmin)