banner = """ 
Mass Add HTTP (Premium Leakers)
"""
print (banner)

def http(url):
	try:
		https = ('http://'+url)
		open('http.txt','a').write(https+'\n'); print(https)
	except: pass


site = input('List Site : ')
ht = open(site, 'r').readlines()
for i in ht:
	try:
		siten = i.strip()
		data=http(siten)
	except: pass