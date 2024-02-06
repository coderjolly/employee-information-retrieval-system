# importing required libraries
import time

import pandas as pd
from sodapy import Socrata

from config_class import Config

# defining a class Extract which has methods to pull data from API and return a dataframe.
class Extract:
    def __init__(self):
        self.configObj = Config()
        self.config_df = self.configObj.read_config()

    def get_data(self):
        # Create the client to point to the API endpoint
        # the API call requires data url, data token, dataset id
        data_url, app_token, data_set = (
            self.configObj.get_data_url(self.config_df),
            self.configObj.get_token(self.config_df),
            self.configObj.get_dataset(self.config_df),
        )
        client = Socrata(data_url, app_token)
        # we are setting timeout of 200 seconds untill failure
        client.timeout = 200
        start_time = time.time()
        #  we are setting a limit of 100000 records
        results = client.get(data_set, limit=100000)
        print(f"--- {time.time() - start_time} seconds ---")
        return pd.DataFrame.from_records(results)
