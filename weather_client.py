import requests
from datetime import datetime
import time
import logging
class WeatherDataClient:
    def __init__(self):
        self.data = {} 
    def __repr__(self):
        return (f"{self.data}")
    def _fetch_location(self) -> tuple:
        try:
            logging.info('Try to take clients IP')
            url_cordinates = 'https://ipapi.co/json/'
            response_self_cord = requests.get(url_cordinates)
            d_cord = response_self_cord.json()
            return {
                "lat": d_cord.get('latitude'),
                "lon": d_cord.get('longitude'),
                "city": d_cord.get('city')
            }
            
        except Exception as e:
            logging.warning("Can't take IP for client location")
            return None 
    def _fetch_raw_data(self, lat, lon) -> dict:
        try:
            logging.info("Conecting with free weather API")
            url = (f"https://api.open-meteo.com/v1/forecast")
            param = {"latitude": lat,
                    "longitude": lon,
                    "current_weather": "true",
                    "timezone": "auto"
                    }
            response = requests.get(url, params=param, timeout=10)
            if response.status_code == 200:
                logging.info("Succsessful conection to weather  API's")
                return response.json().get('current_weather')
            
          
        except Exception as e:
            logging.warning(f"{e}Something wrong with acceptance from API")
            return None
    def get_weather_summary(self):
        loc = self._fetch_location()
        if loc is None:
            logging.warning("--- Warning: Using hardcoded location (Lviv) ---")
            loc = {"lat": 49.8383, "lon": 24.0232, "city": "Lviv (Manual)"}
        atemps = 0   
        while atemps < 3:
            atemps +=1
            weather = self._fetch_raw_data(loc["lat"], loc["lon"])
            
            if not weather:
                logging.error(f"Attempt {atemps} failed")
                if atemps < 3:
                    time.sleep(30)
                    continue
                else:
                    return None
            self.data = {'timestamp': datetime.now().isoformat(),'lat': loc["lat"],'lon': loc["lon"],'city': loc['city'],'temp': weather.get('temperature'),'windspeed': weather.get('windspeed')}
            logging.debug(f"had {self.data} info")
            logging.info("Succsessful get data extraction from weather  API's")
            return self.data
        
