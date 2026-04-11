from weather_client import WeatherDataClient
from processor import DataProcessing
from storage import Storage
import logging
if __name__ == '__main__':
    
    '''new_data_from_api = {
        'timestamp': '2026-04-08T11:11:52.958099', 
        'lat': 49.839, 'lon': 24.0191, 
        'city': 'Kyi', 'temp': 5.3, 
        'windspeed': 9.0
    }
    '''
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler("weather_project.log"),
            logging.StreamHandler()
        ]
    )
    client = WeatherDataClient()
    weather_data = client.get_weather_summary()
    if weather_data is None:
        logging.warning("Date from API's empty. Verify connection")
        exit()

    pandas_procesed = DataProcessing(weather_data)
    final_pandas = pandas_procesed.run_all()
    if final_pandas is not None:
        logging.info("Final local data frame complied")
        storage = Storage(final_pandas)
        storage.to_csv() 
        storage.to_bigquery()
    else:
        logging.warning("data is duplicated")
        exit()