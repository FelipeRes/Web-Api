import httplib2
import json

def getGeocodelocation(inputSting):
	google_api_key = "AIzaSyDAwvqZ6GZsx36idcnG8BelcPHfgsJMxEM"
	locationString = inputSting.replace(" ", "+")
	url ='https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(locationString, google_api_key)
	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)
	latitude = result['results'][0]['geometry']['location']['lat']
	longitude = result['results'][0]['geometry']['location']['lng']
	return (latitude, longitude)
