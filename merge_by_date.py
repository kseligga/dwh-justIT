import pandas as pd
import os
from datetime import datetime, timedelta

# dane źródłowe powinny być w folderze /JustITcsv

start_date = input('Enter start date (%Y-%m-%d): ')
end_date = input('Enter end date (%Y-%m-%d): ')

start_date = datetime.strptime(start_date, '%Y-%m-%d')
end_date = datetime.strptime(end_date, '%Y-%m-%d')

output_file_name = 'data_from_' + str(start_date.strftime('%Y-%m-%d')) + '_to_' + str(end_date.strftime('%Y-%m-%d')) + '.csv'

PATH = 'JustITcsv'
delta = timedelta(days=1)
df_list = []
while start_date <= end_date:
    print(start_date)
    folder = os.path.join(PATH, start_date.strftime('%Y-%m'))
    file_name = start_date.strftime('%Y-%m-%d') + '.csv'
    file_path = os.path.join(folder, file_name)
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df_list.append(df)
    start_date += delta
    
merged_df = pd.concat(df_list, ignore_index=True)
merged_df.to_csv(output_file_name, index=False)
