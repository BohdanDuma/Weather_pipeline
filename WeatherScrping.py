import requests

class WeatherDataClient:
    """
    Клас для взаємодії з OpenWeatherMap API.
    """
    
    def __init__(self, api_url: str):
        self.url = api_url
        self.dict_city = {
        'Kiyv': (50.4024, 30.5322),
        'Tokyo': (35.652832, 139.839478)
        }
    def _build_params(self, lat: float, lon: float) -> str:
        

    def fetch_raw_data(self, city_name: str) -> dict:
        response = requests.get(url)
        data = response.json()
        temp = data['current_weather']['temperature']
        print(temp)
        pass

    def get_weather_summary(self, city_name: str) -> dict:
        """
        Головний метод. Викликає fetch_raw_data та 
        фільтрує дані, залишаючи лише необхідні поля.
        """
        pass
url = "https://api.open-meteo.com/v1/forecast?latitude=49.83&longitude=23.94&current_weather=true"

response = requests.get(url)
data = response.json()
temp = data['current_weather']['temperature']
print(temp)
url_cordinates = 'https://ipapi.co/json/'
response_self_cord = requests.get(url_cordinates)
d_cord = response_self_cord.json()
lat = data.get('latitude')
lon = data.get('longitude')
city = data.get('city')
print(lat, lon)