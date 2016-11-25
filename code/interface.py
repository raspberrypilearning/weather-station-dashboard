import scratch
from requests import get
import json
s = scratch.Scratch()


def listen():
    while True:
        try:
            yield s.receive()
        except scratch.ScratchError:
            raise StopIteration


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

for msg in listen():
    if 'id' in msg['sensor-update']:
        id = msg['sensor-update']['id']
        url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestwsdata/' + id
        weather = get(url).json()['items'][0]
        town, country = getplace(weather['weather_stn_lat'],weather['weather_stn_long'])
        s.sensorupdate({'air_pressure':weather['air_pressure']})
        s.sensorupdate({'wind_gust_speed':weather['wind_gust_speed']})
        s.sensorupdate({'wind_direction':weather['wind_direction']})
        s.sensorupdate({'reading_timestamp':weather['reading_timestamp']})
        s.sensorupdate({'wind_speed':weather['wind_speed']})
        s.sensorupdate({'air_quality':weather['air_quality']})
        s.sensorupdate({'ground_temp':weather['ground_temp']})
        s.sensorupdate({'humidity':weather['humidity']})
        s.sensorupdate({'weather_stn_lat':weather['weather_stn_lat']})
        s.sensorupdate({'weather_stn_long':weather['weather_stn_long']})
        s.sensorupdate({'ambient_temp':weather['ambient_temp']})
        s.sensorupdate({'rainfall':weather['rainfall']})
        s.sensorupdate({'town':town.replace(' ','-')})
        s.sensorupdate({'country':country.replace(' ','-')})
