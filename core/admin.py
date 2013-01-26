
from django.contrib import admin
from core.models import Hotspot, Note
from tastypie.models import ApiAccess, ApiKey

admin.site.register(Hotspot)
admin.site.register(Note)

admin.site.register(ApiAccess)
admin.site.register(ApiKey)