import pandas as pd

from pathlib import Path


INPUT_FILE = Path("input.csv")
OUTPUT = Path("output")

df = pd.read_csv(INPUT_FILE)

before_size = df.size
df = df.drop_duplicates()

print(before_size, df.size, sep=" => ")

grouped = df.groupby('id')

result_dataframes = {}
for group_name, group_data in grouped:
    result_dataframes[group_name] = group_data.copy()

    group_data.to_csv(Path(OUTPUT, group_name + ".csv"), index=False) 

print(result_dataframes)

print(df.head())
