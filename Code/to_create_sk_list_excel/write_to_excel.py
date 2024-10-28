import pandas as pd
import sys
import os
import glob

writer = pd.ExcelWriter('combined.xlsx')
for file_name in glob.glob("data/*.csv"):
    print(file_name)
    df = pd.read_csv(file_name, skip_blank_lines=True, encoding='unicode_escape').drop_duplicates()
    print(df.head(20))
    sheet_name = file_name.split("\\")[1].replace(".csv","").capitalize()
    df.to_excel(writer,sheet_name=sheet_name)
writer._save()