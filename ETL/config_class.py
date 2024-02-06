import pandas as pd


# class to return configuration file data
class Config:
    def __init__(self):
        pass

    # function to read the config.csv file
    def read_config(self):
        return pd.read_csv("configs.csv", quotechar="'")

    # function to get the data url from where we are fetching the data
    def get_data_url(self, config_df):
        return config_df.query(
            'operation == "Datapull" & configname == "data_url"'
        ).value.values.tolist()[0]

    # function to get the dataset id for the project
    def get_dataset(self, config_df):
        return config_df.query(
            'operation == "Datapull" & configname == "data_set"'
        ).value.values.tolist()[0]

    # function to get the database name where we will be saving the data
    def get_database(self, config_df):
        return config_df.query(
            'operation == "Datapull" & configname == "database"'
        ).value.values.tolist()[0]

    # function to get the unique user token to access the Data repository
    def get_token(self, config_df):
        return config_df.query(
            'operation == "Datapull" & configname == "app_token"'
        ).value.values.tolist()[0]
