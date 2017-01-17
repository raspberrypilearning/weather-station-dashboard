## Clean this up by turning the sensor updates into a function call

import scratch
from requests import get
import json
from pprint import pprint
from random import choice

s = scratch.Scratch()

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
station_list = get(stations).json()['items']
for station in station_list:
    station['weather_stn_name'] = station['weather_stn_name'].encode('utf-8')
pprint(station_list)

def listen():
    while True:
        try:
            yield s.receive()
#            print(s.receive())
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
        try:
            weather = get(url).json()['items'][0]
            try:
                town, country = getplace(weather['weather_stn_lat'],weather['weather_stn_long'])
            except:
                town = 'Unknown'
                country = 'Unknown'
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
        except:
            print('Station data not found. Please choose another ID')
    if 'new-station' in msg['broadcast']:
        station_id = choice(station_list)['weather_stn_id']
 #       print(station_id)
        url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestwsdata/' + str(station_id)
        weather = get(url).json()['items']
#        print(weather)
        while not weather:
#            print('New Station Requested')
            station_id = choice(station_list)['weather_stn_id']
#            print(station_id)
            url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestwsdata/' + str(station_id)
            weather = get(url).json()['items']
        try:
            town, country = getplace(weather[0]['weather_stn_lat'],weather[0]['weather_stn_long'])
        except:
            town = 'Unknown'
            country = 'Unknown'
        s.sensorupdate({'air_pressure':weather[0]['air_pressure']})
        s.sensorupdate({'wind_gust_speed':weather[0]['wind_gust_speed']})
        try:
            s.sensorupdate({'wind_direction':weather[0]['wind_direction']})
        except:
            s.sensorupdate({'wind_direction':0})
        s.sensorupdate({'reading_timestamp':weather[0]['reading_timestamp']})
        s.sensorupdate({'wind_speed':weather[0]['wind_speed']})
        s.sensorupdate({'air_quality':weather[0]['air_quality']})
        s.sensorupdate({'ground_temp':weather[0]['ground_temp']})
        s.sensorupdate({'humidity':weather[0]['humidity']})
        s.sensorupdate({'weather_stn_lat':weather[0]['weather_stn_lat']})
        s.sensorupdate({'weather_stn_long':weather[0]['weather_stn_long']})
        s.sensorupdate({'ambient_temp':weather[0]['ambient_temp']})
        s.sensorupdate({'rainfall':weather[0]['rainfall']})
        try:
            s.sensorupdate({'town':town.replace(' ','-')})
        except:
            s.sensorupdate({'town':'/'})
        s.sensorupdate({'country':country.replace(' ','-')})



