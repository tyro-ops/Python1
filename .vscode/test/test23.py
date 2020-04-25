import pandas as pd
import pprint

import xlrd

# for an earlier version of Excel, you may need to use the file extension of 'xls'
df = pd.read_excel(r'/Users/yogesh.kalbhore/Desktop/NodeCapacity.xlsx')
dd = pd.read_json('/Users/yogesh.kalbhore/Desktop/untitled.json')
print(df)
print(dd)
