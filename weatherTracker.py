import requests
import json

url = 'http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&appid={2}&units={3}'
apiKey = '58c9d832ec69e6fd8f85409e16cd356d'
units = 'imperial'
snoqualmieLat, snoqualmieLon = 47.410694, -121.410227
crystalLat, crystalLon = 46.935568, -121.474292

# Build the api request urls
snoqualmieBuiltUrl = url.format(snoqualmieLat, snoqualmieLon, apiKey, units)
crystalBuiltUrl = url.format(crystalLat, crystalLon, apiKey, units)

# Make the request to weather service
snoqualmieRequest = requests.get(snoqualmieBuiltUrl)
crystalRequest = requests.get(crystalBuiltUrl)

# Convert the response to JSON for parsing
snoqualmieJson = json.loads(snoqualmieRequest.text)
crystalJson = json.loads(crystalRequest.text)

# Extract necessary fields for display on matrix
snoqualmieTemp, snoqualmieFeelsLike = snoqualmieJson['main']['temp'], snoqualmieJson['main']['feels_like']
crystalTemp, crystalFeelsLike = crystalJson['main']['temp'], crystalJson['main']['feels_like']


print(snoqualmieTemp, snoqualmieFeelsLike)
print(crystalTemp, crystalFeelsLike)
print('--------------------------------')
print('Snoqualmie result:', snoqualmieJson, '\n')
print('Crystal result:', crystalJson)