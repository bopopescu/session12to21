# Web Service for Weather : https://openweathermap.org/api
# Web Service for News : https://newsapi.org/

# import requests
import requests as rq
import json as js

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=b278eb0105a14101be81556ed0585a27')
response = rq.get(url)
# print(response.text)
# print(type(response))

newsData = js.loads(response.text)
print(newsData)
print(type(newsData))
# JSON Parsing
print(newsData['articles'][0])
print(newsData['articles'][0]['source']['name'])
print(newsData['articles'][0]['author'])
print(newsData['articles'][0]['title'])