import requests

API_KEY = '0542406d58c610dc304291ea6cc19e21'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# city = input('Enter your city"s name: ')
city = 'Johannesburg'

request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
# print(request_url)

response = requests.get(request_url)
# print(response.json())

if response.status_code == 200:
    data = response.json()
    # print(data)
    weather = data['weather'][0]['description']
    print(weather)
    temp = data['main']['temp'] - 273.15
    print(temp)
else:
    print('Errror check shit')