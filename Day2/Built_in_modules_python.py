
import pandas as pd

import os
data=r"D:\Grid3\test.csv"

data_read=pandas.read_csv(data)
print (data_read.head())

print(os.getcwd())


