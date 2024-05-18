import pandas as pd
import os
from datetime import datetime, timedelta

# dane źródłowe powinny być w folderze /JustIT

start_date = datetime.strptime('2021-10-23', '%Y-%m-%d')
end_date = datetime.strptime('2023-09-25', '%Y-%m-%d')

INPUT_PATH = 'JustIT'
OUTPUT_PATH = 'JustITcsv'
if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

delta = timedelta(days=1)
while start_date <= end_date:
    print(start_date)
    folder_name = start_date.strftime('%Y-%m')
    folder = os.path.join(INPUT_PATH, folder_name)
    output_folder = os.path.join(OUTPUT_PATH, folder_name)
    bare_file_name = start_date.strftime('%Y-%m-%d')
    file_name = bare_file_name + '.json'
    output_file_name = bare_file_name + '.csv'
    file_path = os.path.join(folder, file_name)
    file_output_path = os.path.join(output_folder, output_file_name)
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    if os.path.exists(file_path):
        data = pd.read_json(file_path)
        data.to_csv(file_output_path, index=False)
    start_date += delta
