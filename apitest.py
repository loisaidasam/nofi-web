import json
from pprint import pprint
import urllib
import urllib2

try:
	# Add user
#	url = 'http://nofiweb:8052/api/v1/user/?format=json'
#	
#	values = {
#		'username': 'testuser4',
#	}
	
	
	# Add
	url = 'http://nofiweb:8052/api/v1/hotspot/?format=json&username=testuser4&api_key=a8bb01d6d12d18b09a430150d81d6650a1e07a5d'
	
	# Update
	#url = 'http://nofiweb:8052/api/v1/hotspot/12/?format=json'
	
	values = {
		"created_by": "/api/v1/user/8/",
		'latitude': 46.056451,
		'longitude': 14.50807,
		'ssid': 'foo on the barZ!',
	}

	data = json.dumps(values)
	req = urllib2.Request(url, data)
	req.add_header('Content-Type', 'application/json')
	
	# For update
	#req.get_method = lambda: 'PUT'
	
	response = urllib2.urlopen(req)
	
	print response.code, response.msg
	#print response.read()
	data = json.loads(response.read())
	pprint(data)
	
	#print response.code, response.msg, response.url
	#pprint(response.__dict__)
	
except Exception, e:
	print e.read()
	raise

