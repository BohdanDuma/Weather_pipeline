from WeatherScrping import WeatherDataClient
import pandas as pd
import numpy as np
import platform
class DataProcessing:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.df, self.last_str = self._load()
    def _load(self):
        df = pd.DataFrame(self.dictionary)
        try:
            last_str = pd.read_json('last_state.json')
            last_str = last_str.tail()
            return df, last_str
        except Exception as e:
            print("can't take csv to extract last")
            return None
        
    
        
    def _compare_cur_last(self):
        cur_time = self.df['timestamp'].iloc(-1) 
        last_time = self.last_str['timestamp']
        cur_temp = self.df['temp'].iloc[-1]
        last_temp = self.last_str['temp']
        if cur_time == last_time and cur_temp == last_temp:
            return None #тут логінг
        else:
            return self.df
         
    def _add_new_columns(self):
        if  self._compare_cur_last():
            self.df['windy'] = np.where(self.df['windspeed'] > 10, 'Yes', 'No')
            self.df['platform'] = platform.node()
            return self.df
        else:
            return None
    