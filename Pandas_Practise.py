# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:00:11 2019

@author: Training28
"""

import pandas as pd

orders_df=pd.DataFrame()
orders_df['customers_id']=[1,1,1,1,1,2,2,3,3,3,3,3]
orders_df['Order_id']=[1,1,1,2,2,3,3,4,5,6,6,6]
print(orders_df)
count_no_of_orders=lambda x:len(x.unique())
orders_df['no_of_orders_per_client']=(orders_df
                                     .groupby(['customers_id'])['Order_id']
                                     .transform(count_no_of_orders))
print(orders_df)

def multiple_items_per_order(_items):
    multiple_item_bool = _items.duplicated(keep=False)
    return(multiple_item_bool)

orders_df['item_duplicated_per_order'] = (orders_df
                                         .groupby(['Order_id'])['item'] 
                                         .transform(multiple_items_per_order))
print(orders_df)


import numpy as np
import pandas as pd
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s
dates = pd.date_range('20180528', periods=6)
dates
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df




from sqlalchemy import create_engine
engine = create_engine('sqlite://Northwind.sqlite')

