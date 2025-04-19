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

print(data)



# save the changes to data
data.to_csv(r'DVC\data\sample.csv',index=False)

print(f"changes made to the data")