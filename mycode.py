import pandas as pd
import os

data = {
    'Name':['John', 'Bob Dylan', 'Raj'],
    'Age':[23, 24, 25],
    'City': ['New York', 'Chicago', 'Mumbai']
}

df = pd.DataFrame(data)
new_row_loc = {'Name': 'Anup', 'Age': 40, 'City':'Pune'}
df.loc[len(df.index)] = new_row_loc

new_row_loc2 = {'Name': 'Amit', 'Age':28, 'City': 'Delhi'}
df.loc[len(df.index)] = new_row_loc2

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index = False)
print(f"CSV file added to {file_path}")

