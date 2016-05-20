import requests, os, sys, json


proxies = {
	'http':'http://172.16.21.104:808',
	'https':'http://172.16.21.104:808',
	}

lat=25.429808
lon=81.770305
cnt = 3
location = "Allahabad"
api = 'adc4403b31c7aaf588a70f62634ba067'
id=1278994
url = 'http://api.openweathermap.org/data/2.5/forecast/city?id=%d&cnt=3&APPID=%s' %(id, api)

res = requests.get(url, proxies=proxies)
res.raise_for_status()

#print res.text

data = json.loads(res.text)
days = ['Today', 'Tomorrow', 'Day After Tomorrow']
w = data['list']
print 'City : ', location
for i in range(3):
	print days[i]
	print 'Weather: ',w[i]['weather'][0]['main'], '-', w[i]['weather'][0]['description']
	print 'Temperature: ', w[i]['main']['temp']-273.16
	print "Humidity :" , w[i]['main']['humidity']
	print "Wind : speed-", w[i]['wind']['speed'], 'direction', w[i]['wind']['deg']
	print ' '
