
import pandas as pd
import os
from datetime import datetime, timedelta

# skrypt do przeprocesowania jsonów do jednej csv [ta csv waży 5,81 GB xd]
# dane źródłowe powinny być w folderze /JustIT


start_date = datetime.strptime('2021-10-23', '%Y-%m-%d')
end_date = datetime.strptime('2023-09-25', '%Y-%m-%d')


f = open('all_data.csv', 'a')

# Iterate over each date in the range
delta = timedelta(days=1)
while start_date <= end_date:
    print(start_date)
    # Construct the file path
    folder = os.path.join('JustIT', start_date.strftime('%Y-%m'))
    file_name = start_date.strftime('%Y-%m-%d') + '.json'
    file_path = os.path.join(folder, file_name)

    # Check if the file exists
    if os.path.exists(file_path):
        # Load the JSON file into a DataFrame
        data = pd.read_json(file_path)


        data.to_csv('all_data.csv', mode='a', header=f.tell() == 0, index=False)


    start_date += delta
f.close()