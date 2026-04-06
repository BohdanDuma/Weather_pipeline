import requests

class WeatherDataClient:
    def __init__(self):
        self.lat, self.lon, self.city = self._build_params()
        self.timestamp, self.temp, self.windspeed =  self._fetch_raw_data()  
    def __repr__(self):
        return "{'timestamp': '2026-04-06 11:20:00','city': 'Lviv','temp': 8.3,'windspeed': 12.5,'lat': 49.8,'lon': 24.0}"
    def _build_params(self) -> tuple:
        try:
            url_cordinates = 'https://ipapi.co/json/'
            response_self_cord = requests.get(url_cordinates)
            d_cord = response_self_cord.json()
            lat = d_cord.get('latitude')
            lon = d_cord.get('longitude')
            city = d_cord.get('city')
            if lat is None or lon is None:
                raise ValueError('API not give cord')
            return lat, lon, city
        except Exception as e:
            raise RuntimeError(f"Error geo: {e}")
    def _fetch_raw_data(self) -> dict:
        url = (f"https://api.open-meteo.com/v1/forecast?latitude={self.lat:.4f}&longitude={self.lon:.4f}&current_weather=true&timezone=auto")
        response = requests.get(url)
        data = response.json()
        temp = data['current_weather']['temperature']
        timestamp = data['current_weather']['time']
        windspeed = data['current_weather']['windspeed']
        return timestamp, temp, windspeed
        
    def get_weather_summary(self):
        """
        Головний метод. Викликає fetch_raw_data та 
        фільтрує дані, залишаючи лише необхідні поля.
        """
        pass
        
if __name__ == "__main__":
    first = WeatherDataClient()
    print(first)