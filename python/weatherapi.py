import json
import requests 

print('Please enter your zip code')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=47025,us&appid=023094de98871857a8f2714c7bb84281' % zip)
data=r.json()
print(data['weather'][0]['description'])