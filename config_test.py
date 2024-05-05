# host = "localhost"
# user = "postgres"
# password = "IAmBig"
# db_name = "postgres"
# # port = 8080
import pandas as pd

date = pd.date_range(start='2024-03-01', end='2024-03-31')

print(len(date))