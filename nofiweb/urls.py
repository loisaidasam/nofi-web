
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin

from tastypie.api import Api

from core.api import UserResource, HotspotResource


admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(HotspotResource())

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'nofiweb.views.home', name='home'),
	# url(r'^nofiweb/', include('nofiweb.foo.urls')),
	
	url(r'^admin/', include(admin.site.urls)),
	
	(r'^api/', include(v1_api.urls)),
)
