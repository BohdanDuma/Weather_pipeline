from WeatherScrping import WeatherDataClient
from proces import DataProcessing
from storage import Storage
if __name__ == '__main__':
    
    '''new_data_from_api = {
        'timestamp': '2026-04-08T11:11:52.958099', 
        'lat': 49.839, 'lon': 24.0191, 
        'city': 'Kyi', 'temp': 5.3, 
        'windspeed': 9.0
    }
    '''
    date_from_api = WeatherDataClient()
    pandas_procesed = DataProcessing(date_from_api.get_weather_summary())
    final_pandas = pandas_procesed.run_all()
    
   
    if final_pandas is not None:
        storage = Storage(final_pandas)
        storage.to_csv() 
        storage.to_bigquery()
       
    else:
        print("data is duplicate")