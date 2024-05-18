# skrypcik do sprawdzenia jakie są firmy, ile ich jest, ile się przecina

import pandas as pd
import csv
from collections import Counter


# wyciąganie unique
def get_unique_companies(filename):
    unique_companies = set()
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        if 'company_name' in header:
            company_index = header.index('company_name')
            for row in reader:
                try:
                    unique_companies.add(row[company_index])
                except IndexError:
                    print(f"Skipping line {reader.line_num} due to inconsistent number of columns")
    return unique_companies


unique_companies = get_unique_companies('all_data.csv')


pd.Series(list(unique_companies)).to_csv('unique_companies.csv', index=False)


# firmy z przecięcia ręcznie wrzucone do pliku listed.csv. w excelu zmapowane do postaci takiej jak w pliku justIT.
# teraz wyciągamy dane z justit dla tych firm:
def write_matching_companies(data_filename, listed_filename, output_filename):
    # Load the listed companies
    with open(listed_filename, 'r', encoding='utf-8') as f:
        listed_companies = set(line.strip() for line in f)

    with open(data_filename, 'r', encoding='utf-8') as f, open(output_filename, 'w', newline='', encoding='utf-8') as out_file:
        reader = csv.reader(f)
        writer = csv.writer(out_file)
        header = next(reader)
        if 'company_name' in header:
            company_index = header.index('company_name')
            writer.writerow(header)
            for row in reader:
                try:
                    if row[company_index] in listed_companies:
                        writer.writerow(row)
                except IndexError:
                    print(f"Skipping line {reader.line_num} due to inconsistent number of columns")

write_matching_companies('all_data.csv', 'listed.csv', 'all_listed_data.csv')

# liczenie przypadków występowania:
def count_company_names(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        if 'company_name' in header:
            company_index = header.index('company_name')
            company_counter = Counter(row[company_index] for row in reader)
            return company_counter

company_counts = count_company_names('all_listed_data.csv')

sorted_counts = sorted(company_counts.items(), key=lambda x: x[1], reverse=True)

for company, count in sorted_counts:
    print(company, count)
