from requests import get
import json
def getplace(lat, lon):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&sensor=false" % (lat, lon)
    j=get(url).json()
    components = j['results'][0]['address_components']
    country = town = None
    for c in components:
        if "country" in c['types']:
            country = c['long_name']
        if "postal_town" in c['types']:
            town = c['long_name']
    return town, country


print(getplace(51.1, 0.1))
print(getplace(51.2, 0.1))
print(getplace(51.3, 0.1))
