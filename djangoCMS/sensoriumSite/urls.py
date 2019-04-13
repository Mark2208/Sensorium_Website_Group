from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from sensoriumSite import views

urlpatterns = [
   url(r'^test/', views.test,name='test'),
   url(r'^index/', views.index,name='index'),
   
]