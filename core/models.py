
from django.contrib.auth.models import User
from django.db import models


class Hotspot(models.Model):
	# Required
	latitude = models.FloatField()
	longitude = models.FloatField()
	
	# Creation/connection info
	created = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User, null=True, blank=True, related_name="hotspot_creator")
	last_connected = models.DateTimeField(null=True, blank=True)
	last_connected_by = models.ForeignKey(User, null=True, blank=True, related_name="hotspot_connector")
	
	# Optional wifi info
	ssid = models.CharField(max_length=255, null=True, blank=True)
	mac_address = models.CharField(max_length=255, null=True, blank=True)
	password_protected = models.BooleanField(default=False)
	password = models.CharField(max_length=255, null=True, blank=True)
	
	# Optional Foursquare info
	foursquare_id = models.CharField(max_length=255, null=True, blank=True)
	foursquare_name = models.CharField(max_length=255, null=True, blank=True)
	foursquare_type = models.CharField(max_length=255, null=True, blank=True)


class Note(models.Model):
	hotspot = models.ForeignKey(Hotspot)
	created = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User, null=True, blank=True, related_name="note_creator")
	note = models.TextField()

