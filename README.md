# Web-Api
Esse e um projeto para testar conxão com 3 apis diferentes em python
## [HG Weather](https://hgbrasil.com/status/weather/)
API para monitoramento climático e gratuito. Ela obtem dados por código da cidade, por GeoIP, geolocalização, nome da cidade. Para utilizar, é necessário se registrar e adicionar uma chave na url do código.
O exemplo abaixo mostra como fazer a requisicao com python e a bibliteca httplib2:
```python
def getClimaCidade(cidade):
	key = 'sua_chave'
	url = 'https://api.hgbrasil.com/weather/?format=json&city_name='+cidade+'&key=sua_chave'
	print (url)
	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)
	temperatura = result['results']['temp']
	print(temperatura)
	return result
```

## [Ip-API](http://ip-api.com/)
API que busca diversos dados de geolocalização através do ip do usuário. Para utilizar, basta adicionar o ip no final da url.
Mostrando a temperatura:
```python
	url = 'http://ip-api.com/json/'+ 'your ip'
	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)
	pais = result['country']
	cidade = result['city']
	lat = result['lat']
	lon = result['lon']
	print('Pais: '+ str(pais)+'\nCidade: '+str(cidade) +'\nLatitude: '+ str(lat) + '\nLongitude: '+str(lon))
```
## [Github API](https://developer.github.com/v3/)
API para acesso a projetos no github, muito boa para criar extensões da plataforma. Pode ser utilziada através da autenticação direto no header do cabeçalho HTTP.
Exemplo:
```python
  username = 'FelipeRes'
	password = 'Sua Senha'
	auth = base64.encodestring(('%s:%s' % (username,password)).encode()).decode().replace('\n', '')
	url = 'https://api.github.com/user'
	print("url: "+url)
	h = httplib2.Http()
	response, content = h.request(url, 'GET', headers = { 'Authorization' : 'Basic ' + auth })
	result = json.loads(content)
	return result
```


