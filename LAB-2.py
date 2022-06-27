import pandas as pd
import numpy as np
import copy
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer
df=pd.read_csv("2.csv")
print(df['Rower'])
a=LabelEncoder()
df['Rower']=a.fit_transform(df['Rower'])
print(df['Rower'])
b=LabelBinarizer()
df=b.fit_transform(df['Rower'])
print(df)
