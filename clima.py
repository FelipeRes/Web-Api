import httplib2
import json

def getClimaCidade(cidade):
	key = 	'ead2d1fa'
	url = 'https://api.hgbrasil.com/weather/?format=json&city_name='+cidade+'&key=ead2d1fa'
	print (url)
	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)
	temperatura = result['results']['temp']
	print(temperatura)
	return result
	
