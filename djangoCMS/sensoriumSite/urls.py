from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from sensoriumSite import views

urlpatterns = [
   url(r'^test/', views.test,name='test'),
   url(r'^index/', views.index,name='index'),
   url(r'^about_us/', views.about_us,name='about_us'),
   url(r'^projects/', views.projects,name='projects'),
  
   
]