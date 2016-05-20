import requests, bs4

proxies = {
	'http':'http://172.16.21.104:808',
	'https':'http://172.16.21.104:808',
	}


res = requests.get('https://quora.com', proxies=proxies)

print res.raise_for_status()
print res.status_code

bs = bs4.BeautifulSoup(res.text, "lxml")
print type(bs)