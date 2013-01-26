
import logging

from django.contrib.auth.models import User
from django.db import models
from tastypie import fields
from tastypie.authentication import Authentication, ApiKeyAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.models import create_api_key
from tastypie.resources import ModelResource

from core.models import Hotspot, Note

logger = logging.getLogger(__name__)


class UserResource(ModelResource):
	apikey = fields.CharField()
	
	class Meta:
		queryset = User.objects.all()
#		resource_name = 'user'
		fields = ['apikey', 'username', 'email', 'last_login', 'date_joined']
		always_return_data = True
		authentication = Authentication()
		authorization = Authorization()
		
#		excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
#		allowed_methods = ['get', 'post']

	def dehydrate_apikey(self, bundle):
		try:
			return bundle.obj.api_key.key
		except:
			pass
		return None


class HotspotResource(ModelResource):
	created_by = fields.ForeignKey(UserResource, 'created_by')

	class Meta:
		queryset = Hotspot.objects.all()
#		resource_name = 'hotspot'
#		allowed_methods = ['get', 'post']
		authentication = ApiKeyAuthentication()
		authorization = DjangoAuthorization()
#		authorization = Authorization()
		always_return_data = True


models.signals.post_save.connect(create_api_key, sender=User)