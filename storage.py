import pandas as pd
from pathlib import Path
import time
import os
from google.cloud import bigquery
class Storage:
    def __init__(self,df_str_to_save):
        self.df_str_to_save = df_str_to_save
        self.client = bigquery.Client.from_service_account_json("credentials.json")
        self.table_id = "smart-seer-481909-d1.weather_monitor.weather_stats"
    def _to_json(self): 
        self.df_str_to_save.to_json('last_state.json',orient='records', date_format='iso')
    def to_bigquery(self):
        try:

            job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND",autodetect=True)
            job = self.client.load_table_from_dataframe( self.df_str_to_save, self.table_id, job_config=job_config )
            job.result()
            print("Welldone!")
        except Exception as e:
            print(f'Exception {e} with bigquery')
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

    