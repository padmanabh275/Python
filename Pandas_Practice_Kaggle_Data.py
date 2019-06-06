# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:00:34 2019

@author: Training28
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Mall_Customers.csv')

df.columns
df.info()
df.describe()
df.head(5)
df.columns=['id','gender','age','income','score']
plt.hist(df.age)
df.boxplot()
df['gender'].value_counts()
df['gender'] = df.gender.map({'Male':1,'Female':0})
sns.barplot(x = 'gender', y = 'score', data = df)
sorted(list(df.age.unique()))
def group_age(age):
    if age <= 30:
        return "<= 30"
    elif age <= 40:
        return "31-40"
    elif age<= 50:
        return "41-50"
    elif age<= 60:
        return "51-60"
    else:
        return "61-70"

df['age']= df.age.apply(group_age)
df
sns.barplot(x = 'age', y = 'score', hue = "gender", data  = df,)
sns.barplot(x = "age",y="income",hue = "gender", data = df, order = ['<= 30', '31-40', '41-50','51-60','61-70'])
plt.scatter(x = "income", y = "score", data = df)
plt.scatter(x = "income", y = "score", data = df[df.gender == 1])
plt.scatter(x = "income", y = "score", data = df[df.gender == 0])
plt.scatter(x = "age", y = "score", data = df[df.gender == 0])
plt.scatter(x = "age", y = "score", data = df[df.gender == 1])
df.groupby(["gender","age"]).mean()
