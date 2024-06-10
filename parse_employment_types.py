import pandas as pd
import ast

df = pd.read_csv('all_listed_data.csv')

def parse_employment_types(employment_types_str):
    employment_types = ast.literal_eval(employment_types_str)
    employment = employment_types[0]
    
    e_type = employment.get('type', None)
    salary = employment.get('salary', None)
    salary_from = None
    salary_to = None
    currency = None
    if salary is not None:
        salary_from = salary.get('from', None)
        salary_to = salary.get('to', None)
        currency = salary.get('currency', None)
    return {'type': e_type, 'salary_from': salary_from, 'salary_to': salary_to, 'currency': currency}

def create_new_columns(df):
    parsed_data = df['employment_types'].apply(parse_employment_types)
    new_data = parsed_data.apply(pd.Series)
    for col in new_data.columns:
        df[col] = new_data[col]
    

create_new_columns(df)

df.to_csv('all_listed_data_parsed.csv', index=False)
