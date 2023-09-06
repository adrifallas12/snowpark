from snowflake.snowpark.session import Session
import pandas as pd

# import sf credentials
import configparser
config_file = 'sf_creds.config'
config = configparser.ConfigParser()
config.read(config_file)


connection_parameters = {
    "account": config['DEFAULT']['SQCOROF-MX53774'],
    "user": config['DEFAULT']['Adriana Fallas'],
    "password": config['DEFAULT']['TexasTech2023'],
    "role": config['DEFAULT']['data_science'],
    "warehouse": config['DEFAULT']['ds_warehouse'],
    "database": config['DEFAULT']['snowpark_capstone_db'],
    "schema": config['DEFAULT']['adriana_fallas_schema']
 }

# Create and Verify Session
session = Session.builder.configs(connection_parameters).create()
session.add_packages("snowflake-snowpark-python", "pandas")
