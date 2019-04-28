from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from sensoriumSite import views

urlpatterns = [
   
   url(r'^$', views.index,name='index'),
   url(r'^aboutus/', views.about_us,name='about_us'),
   url(r'^projects/', views.projects,name='projects'),
   url(r'^equipment/', views.equipment,name='equipment'),
   url(r'^newsevents/', views.newsEvents,name='newsEvents'),
   
]