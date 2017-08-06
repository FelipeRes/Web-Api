import httplib2
import json
import base64
import string

def getInfo():
	username = 'FelipeRes'
	password = 'Sua Senha'
	auth = base64.encodestring(('%s:%s' % (username,password)).encode()).decode().replace('\n', '')
	url = 'https://api.github.com/user'
	print("url: "+url)
	h = httplib2.Http()
	response, content = h.request(url, 'GET', headers = { 'Authorization' : 'Basic ' + auth })
	result = json.loads(content)
	return result