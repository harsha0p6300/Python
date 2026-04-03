# import pandas as pd
# data=pd.read_csv('size.csv')
# print(data)

import cs

with open("size.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)          
