import requests
from datetime import datetime
class WeatherDataClient:
    def __init__(self):
        self.data = {} 
    def __repr__(self):
        return (f"{self.data}")
    def _fetch_location(self) -> tuple:
        try:
            url_cordinates = 'https://ipapi.co/json/'
            response_self_cord = requests.get(url_cordinates)
            d_cord = response_self_cord.json()
            return {
                "lat": d_cord.get('latitude'),
                "lon": d_cord.get('longitude'),
                "city": d_cord.get('city')
            }
            
        except Exception as e:
            print(f"Error geo: {e}")
            return None 
    def _fetch_raw_data(self, lat, lon) -> dict:
        try:
            url = (f"https://api.open-meteo.com/v1/forecast")
            param = {"latitude": lat,
                    "longitude": lon,
                    "current_weather": "true",
                    "timezone": "auto"
                    }
            response = requests.get(url, params=param, timeout=10)
            return response.json().get('current_weather')
        except Exception as e:
            print(f"problem with weather extraction {e}")
            return None
    def get_weather_summary(self):
        loc = self._fetch_location()
        if loc is None:
            print("--- Warning: Using hardcoded location (Lviv) ---")
            loc = {"lat": 49.8383, "lon": 24.0232, "city": "Lviv (Manual)"}
            
        
        weather = self._fetch_raw_data(loc["lat"], loc["lon"])   
        if not weather:
            print("Can't extract weather")
            return None
        self.data = {'timestamp': datetime.now().isoformat(),'lat': loc["lat"],'lon': loc["lon"],'city': loc['city'],'temp': weather.get('temperature'),'windspeed': weather.get('windspeed')}
        return self.data
