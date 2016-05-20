import sys, requests, json, threading, time

def get_scores():
	while True:
		res = requests.get('http://cricscore-api.appspot.com/csa?id=%d' %(id), proxies=proxies)
		res.raise_for_status()
		if res.status_code == 304:
			pass
		else:
			data = res.text
			data = json.loads(data)
			print data[0]["de"]
			print " "
			print data[0]["si"]
		time.sleep(60)




proxies = {
	'http':'http://172.16.21.104:808',
	'https':'http://172.16.21.104:808',
}

print "Following are the available matches: \n\n"

res = requests.get('http://cricscore-api.appspot.com/csa', proxies = proxies)
res.raise_for_status()

data = res.text
#print data
data = json.loads(data)

l = len(data)
for i in range(l):
	print `i+1`+') ', data[i]["t1"], 'VS', data[i]["t2"], "\n"

print "\n\nEnter your choice :"

id =input()

while int(id) > l and int(id) <= 0:
	print "Wrong Choice \nEnter Choice No. :"
	id = input()

id = int(id)
id = data[id-1]["id"]
thread = threading.Thread(target=get_scores)
thread.start()