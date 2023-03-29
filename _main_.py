import json
import numpy as np
from faker import Faker
import csv
import json
import random
import sys

import excel2json
import orient as orient
import pandas as pd

fake=Faker()

xl = pd.ExcelFile('File_name')
sheet = xl.sheet_names
# print(sheet)
for item in sheet:
    # print(item)
    excel_data_df = pd.read_excel('File_name',sheet_name= item,index_col=False)
    json_str = excel_data_df.to_json(orient='records')
    json_lt = json.loads(json_str)
    file_name = item + '.csv'
    num_rows= 10
    with open(file_name, mode='w') as file:
        header = [col["Field"] for col in json_lt]
        header_str = ",".join(header)
        file.writelines(header_str + "\n")
        for i in range(num_rows):
            row = []
            for col in json_lt:
                # print(col)
                field = col["Field"]
                col_type = col["Type"]
                if col_type == "String":
                    row.append(str(fake.text()))
                if col_type == "Date":
                    row.append(str(fake.date()))
                if col_type == "Time":
                    row.append(str(fake.date_time()))
                if col_type == "Currency":
                    row.append(str(fake.currency()[0]))
                if col_type == "Integer":
                    row.append(str(fake.random_int()))
                if col_type == "Country":
                    row.append(str(fake.country()))
                if col_type == "Enum":
                    values = col["Accepted Values and Format"]
                    enum_list = values.split("-")
                    if '' in enum_list:
                        enum_list.remove('')
                    enum_choice = random.choice(enum_list).strip()
                    row.append(enum_choice)
            # print(row)
            row_str = ",".join(row)
            file.write(row_str + "\n")
          
