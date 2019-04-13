from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from sensoriumSite.models import TestPlugin
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