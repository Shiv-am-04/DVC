import pandas as pd
import numpy as np


data = pd.read_csv(r'DVC\data\sample.csv')


# Adding new rows to data for version v2
new_row = {
    'Name' : 'Rina',
    'Place' : 'Pune',
    'Age' : 25,
    'Salary' : 14000
}

print(data.loc[len(data)-1])