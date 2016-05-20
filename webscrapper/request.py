import requests

proxies = {
	'http':'http://172.16.21.104:808',
	'https':'http://172.16.21.104:808',
	}


res = requests.get('https://raw.githubusercontent.com/vampcoder/A-star-planning/master/test5.py', proxies=proxies)
print type(res)
print res.status_code == requests.codes.ok
len (res.text)
print res.text
print res.raise_for_status()