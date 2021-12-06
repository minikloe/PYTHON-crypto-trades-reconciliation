#!/usr/bin/env python
# coding: utf-8




import csv
import pandas as pd
import numpy as np





from pandas.core.frame import DataFrame





# load csv file

datacsv = pd.read_csv('/Users/kloe/Desktop/Middle Office Analyst Test data file.csv',index_col=False)





print(datacsv)





df = pd.DataFrame(datacsv)
print(df)





# add an empty column for 'Flag any transfer that started before 8am and finished after 8am.'

df['flag'] = [[] for _ in range(len(df))]




print(df.dtypes)





print(df)





# transfer object type to datatime type

df['time'] = pd.to_datetime(df['time'])




print(df.dtypes)





# Flag any transfer that started before 8am

df['flag'] = np.where(df['time']>'2/25/20 8:00','started b4 8am','')





print(df)





# Flag any transfer that finished after 8am

df['flag'] = np.where(df['time']>'2/25/20 20:00','finished after 8pm','')





print(df)




# Match pairs of withdrawals and deposits as ‘transfers',; 

df.groupby('tx_id').agg(lambda x: x.tolist())



