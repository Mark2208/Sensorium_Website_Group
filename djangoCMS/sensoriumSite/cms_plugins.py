from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from sensoriumSite.models import TestPlugin, Sensorium_Bio, Sensorium_News
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin  # register the plugin
class MainPluginPublisher(CMSPluginBase):
    model = TestPlugin  # model where plugin data are saved
    module = _("sensoriumSite")
    name = _("Test Plugin")  # name of the plugin in the interface
    render_template = "testTemplate.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
		

@plugin_pool.register_plugin  # register the plugin
class UserBioPluginPublisher(CMSPluginBase):
    model = Sensorium_Bio  # model where plugin data are saved
    module = _("sensoriumSite")
    name = _("User Group Bio")  # name of the plugin in the interface
    render_template = "site_template/pluginTemplates/bio.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
		
@plugin_pool.register_plugin  # register the plugin
class NewsPluginPublisher(CMSPluginBase):
    model = Sensorium_News  # model where plugin data are saved
    module = _("sensoriumSite")
    name = _("News/Event")  # name of the plugin in the interface
    render_template = "site_template/pluginTemplates/news_events.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context