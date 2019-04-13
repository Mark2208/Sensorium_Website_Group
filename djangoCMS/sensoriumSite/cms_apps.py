from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register  # register the application
class mainApphook(CMSApp):
    app_name = "sensoriumSite"
    name = "Main Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["sensoriumSite.urls"]
		
