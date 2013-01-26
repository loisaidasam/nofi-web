
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource


from core.models import Hotspot, Note


class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
#		allowed_methods = ['get', 'post']
		always_return_data = True


class HotspotResource(ModelResource):
	created_by = fields.ForeignKey(UserResource, 'created_by')

	class Meta:
		queryset = Hotspot.objects.all()
		resource_name = 'hotspot'
#		allowed_methods = ['get', 'post']
#		authentication = Authentication()
		authorization = Authorization()
		always_return_data = True