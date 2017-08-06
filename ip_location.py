import httplib2
import json

def getLocation():
	url = 'http://ip-api.com/json/'+ 'your ip'
	print("url: "+url)
	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)
	print(result)
	pais = result['country']
	cidade = result['city']
	lat = result['lat']
	lon = result['lon']
	print('Pais: '+ str(pais)+'\nCidade: '+str(cidade) +'\nLatitude: '+ str(lat) + '\nLongitude: '+str(lon))
	return result
	
