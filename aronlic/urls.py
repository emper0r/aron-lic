from django.conf.urls import patterns, include, url
from django.contrib import admin
from Licenza import views

admin.site.site_header = 'Server Licenza per Aron Web Manager'

urlpatterns = patterns('',
    url(r'^', include(admin.site.urls)),
    url(r'^rl/(?P<req>[A-Za-z0-9]{48})/(?P<lic>[A-Za-z0-9]{48})/(?P<pwd>[A-Za-z0-9\+\/\=]{88})/(?P<server_id>[A-Za-z0-9]{32})$', views.activation, name='activate'),
    url(r'^cl/(?P<server_id>[A-Za-z0-9]{32})$', views.check_lic, name='check_id'),
)
