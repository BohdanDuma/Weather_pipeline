import pandas as pd
import numpy as np
import platform
from WeatherScrping import WeatherDataClient
class DataProcessing:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.df = None
        self.state = True
        self.last_str = pd.DataFrame()
    def _load(self):
        self.df = pd.DataFrame([self.dictionary])
        print(self.df.columns.tolist())
        try:
            self.last_str = pd.read_json('last_state.json', orient='records')
            if self.last_str.empty:
                self.state = False  
        except Exception as e:
            print(f"{e} can't take json to extract last")
            self.state = False
        

        
    def _compare_cur_last(self):
        print(f"Доступні колонки: {self.df.columns.tolist()}")
        if not self.state:
            return self.df
        cur_time = pd.to_datetime(self.df['timestamp'].iloc[-1])
        last_time = pd.to_datetime(self.last_str['timestamp'].iloc[-1])
        cur_time_min = cur_time.replace(second=0, microsecond=0)
        last_time_min = last_time.replace(second=0, microsecond=0)
        cur_temp = self.df['temp'].iloc[-1]
        last_temp = self.last_str['temp'].iloc[-1] 
        cur_city = self.df['city'].iloc[-1]
        last_city = self.last_str['city'].iloc[-1]
        if cur_time_min == last_time_min and cur_temp == last_temp and cur_city == last_city:
            return None #тут логінг
        else:
            return self.df
         
    def _add_new_columns(self):
        
        if  self._compare_cur_last() is not None:
            self.df['windy'] = np.where(self.df['windspeed'] > 10, 'Yes', 'No')
            self.df['platform'] = platform.node()
            return self.df
        else:
            return None
    def run_all(self):
        self._load()
        
        return self._add_new_columns()

date_from_api = {'timestamp': '2026-04-09T21:37:34.286596', 'lat': 49.839, 'lon': 24.0191, 'city': 'Lviv', 'temp': 2.0, 'windspeed': 6.8}
pandas_procesed = DataProcessing(date_from_api)
final_pandas = pandas_procesed.run_all()