import pandas as pd
import os

current = os.path.dirname(os.path.realpath(__file__)) + r"\..\rawdata\adult.data"
# print(current)

file = pd.read_csv(current, header=None)
file.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary']
file_obj = file.select_dtypes(['object'])
file[file_obj.columns] = file_obj.apply(lambda x: x.str.strip())

# print(file.head())
print(file.columns[file.stack().str.contains('?', regex=False).any()])


age_contain_quest = file.loc[file['native-country'] == r'?']
# print(age_contain_quest.iloc[1])