import pandas as pd
from pathlib import Path
import time
import os
from google.cloud import bigquery
import logging
from dotenv import load_dotenv
load_dotenv()
class Storage:
    def __init__(self,df_str_to_save):
        self.df_str_to_save = df_str_to_save
        self.client = bigquery.Client()
        self.table_id = os.getenv("BQ_TABLE_ID")
    def _to_json(self): 
        self.df_str_to_save.to_json('last_state.json',orient='records', date_format='iso')
    def to_bigquery(self):
        try:
            job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND",autodetect=True)
            job = self.client.load_table_from_dataframe( self.df_str_to_save, self.table_id, job_config=job_config )
            job.result()
            logging.info("Welldone! Current state loaded to BigQuery")
        except Exception as e:
            logging.warning(f'Problem {e} with bigquery')
    def to_csv(self):
        p = Path('Weather_data.csv')
        count = 0
        while True:
            count += 1
            if count == 3:
                logging.warning('Problem with local csv')
                break
            try:
                if p.exists():
                    self.df_str_to_save.to_csv('Weather_data.csv', mode='a', index=False, header=False)
                    logging.info("Welldone! Current state loaded to local csv")
                else:
                    self.df_str_to_save.to_csv('Weather_data.csv',index=False)
                    logging.info('Create new local csv and added current state')
                self._to_json()    
                break
                
            except Exception as e:
                logging.warning(f"Problem with conection to csv. Wait 10 second to {count} try")
                time.sleep(10)

    