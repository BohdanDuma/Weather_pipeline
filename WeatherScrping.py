import requests

class WeatherDataClient:
    """
    Клас для взаємодії з OpenWeatherMap API.
    """
    
    def __init__(self, api_url: str):
        self.url = api_url
        self.dict_city = 
    def _build_params(self, lat: float, lon: float) -> str:
        pass

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
    def _get_location(self):
        
response = requests.get(url)
data = response.json()
temp = data['current_weather']['temperature']
print(temp)
url_cordinates = 'https://ipapi.co/json/'
response_self_cord = requests.get(url_cordinates)
d_cord = response_self_cord.json()
lat = d_cord.get('latitude')
lon = d_cord.get('longitude')
city = d_cord.get('city')
print(city)