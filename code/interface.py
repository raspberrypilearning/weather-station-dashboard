import pyowm
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

for msg in listen():
    if 'key' in msg['sensor-update']:
        key = msg['sensor-update']['key']
        owm = pyowm.OWM(key)
    if 'location' in msg['sensor-update']:
        location = msg['sensor-update']['location']
        observation = owm.weather_at_place(location)
        w = observation.get_weather()
        temperature = w.get_temperature()['temp']
        rain = w.get_rain()
        if '1h' in rain:
            rainfall = rain['1h']
        else:
            rainfall = 0
        wind = w.get_wind()
        if 'speed'in wind:
            wind_speed = wind['speed']
        else:
            wind_speed = 0
        if 'deg' in wind:
            wind_direction = wind['deg']
        else:
            wind_direction = 0
        clouds = w.get_clouds()
        s.sensorupdate({'temperature': temperature - 273})
        s.sensorupdate({'rainfall': rainfall})
        s.sensorupdate({'wind_speed': wind_speed})
        s.sensorupdate({'wind_direction': wind_direction})
        s.sensorupdate({'clouds': clouds})
