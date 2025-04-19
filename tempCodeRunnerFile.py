import pandas as pd
import numpy as np

data = pd.read_csv(r'DVC\data\sample.csv')

data.reset_index(drop=True,inplace=True)

# Adding new rows to data for version v2
new_row = {
    'Name' : 'Rina',
    'Place' : 'Pune',
    'Age' : 25,
    'Salary' : 14000
}

data.loc[data.shape[0]] = new_row

# Adding new rows to data for version v3

new_rows_2 = [['Mina','Pimpri',22,70000],['Tina','Nashik',25,80000]]

for row in new_rows_2:
    data.loc[data.shape[0]] = row

print(data)