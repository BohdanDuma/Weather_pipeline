import pandas as pd
from pathlib import Path
import time
class Storage:
    def __init__(self,df_str_to_save):
        self.df_str_to_save = df_str_to_save
    def _to_json(self): 
        self.df_str_to_save.to_json('last_state.json', mode='w')
    def to_csv(self):
        p = Path('Weather_data.csv')
        count = 0
        while True:
            count += 1
            if count == 5:
                print('Problem with csv')
                break
                
            try:

                if p.exists():
                    self.df_str_to_save.to_csv('Weather_data.csv', mode='a', index=False, header=False)
                else:
                    self.df_str_to_save.to_csv('Weather_data.csv',index=False)
                    print('file not exist')
                self._to_json()    
                break
                
            except Exception as e:
                print('Problem with conection to csv')
                print('wait 10 second to next try')

                time.sleep(10)

    