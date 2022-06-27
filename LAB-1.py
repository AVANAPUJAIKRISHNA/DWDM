from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
df=pd.read_csv('1.csv')
print(df)
imputer=SimpleImputer(strategy='mean',missing_values=np.nan)
imputer=imputer.fit(df[['day','month','year','temperature']])
df[['day','month','year','temperature']]=imputer.transform(df[['day','month','year','temperature']])
print(df)