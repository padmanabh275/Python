# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:45:03 2019

@author: Training28
"""
import pandas as pd
import sqlalchemy
import urllib
quoted = urllib.parse.quote_plus('Driver={SQL Server Native Client 11.0};'
                'Server=ssintr02;'
                'Database=T5_Padmanabh;'
                'uid=T5_Padmanabh;'
                'pwd=Bills@275;')
engine=sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))

sql='select * from roads'
df=pd.read_sql(sql,engine)
print(df)

df.to_sql('trial1',con=engine,if_exists='replace',index=False) #/replace
print(test2)




