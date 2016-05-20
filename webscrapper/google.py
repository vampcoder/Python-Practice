import os, sys, webbrowser, bs4, requests,time

searchText ="Amol Upraity"
proxies = {
	'http':'http://172.16.21.104:808',
	'https':'http://172.16.21.104:808',
	}

str = searchText.split()
str = '+'.join(str)

res = requests.get('http://google.com/search?q='+str, proxies=proxies)

if res.status_code == requests.codes.ok:
    bs = bs4.BeautifulSoup(res.text, "lxml")
    links = bs.select('.r a')
    num = min(5, len(links))
    print len(links)
    num = len(links)
    for i in range(num):
        webbrowser.open('http://google.com' + links[i].get('href'))
        time.sleep(.5)