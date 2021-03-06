#!/usr/bin/env python

import urllib.request, json

city = "Alexandria,eg"
api_key = ""
units = "metric"
unit_key = "C"

weather = eval(str(urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units={}".format(city, api_key, units)).read())[2:-1])

info = weather["weather"][0]["description"].capitalize()
temp = int(float(weather["main"]["temp"]))

print("%i°%s" % (temp, unit_key))
