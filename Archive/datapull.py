import pandas as pd
from sodapy import Socrata
import time

configdf = pd.read_csv("configs.csv")
data_url = configdf.query('operation == "Datapull" & configname == "data_url"').value.values.tolist()[0]
data_set = configdf.query('operation == "Datapull" & configname == "data_set"').value.values.tolist()[0]
app_token = configdf.query('operation == "Datapull" & configname == "app_token"').value.values.tolist()[0]
data_staging = configdf.query('operation == "Datapull" & configname == "staginglocation"').value.values.tolist()[0]

def get_data(data_url,app_token,data_set):
    # Create the client to point to the API endpoint
    client = Socrata(data_url,app_token)
    client.timeout = 200

    start_time = time.time()
    results = client.get(data_set, limit=10000000)
    print(f"--- {time.time() - start_time} seconds ---")

    return pd.DataFrame.from_records(results)

df_data = get_data(data_url,app_token,data_set)
# saved as csv in local folder for cleaning purposes
df_data.to_csv(data_staging + "NYC_payroll_data.csv")