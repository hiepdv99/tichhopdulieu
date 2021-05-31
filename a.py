import pandas as pd
from pandas import DataFrame

df = pd.read_csv('cleantopcv.csv')

df.columns =[ 'company', 'title',  'date','salary','workingform','target','position','experience','sex','city']
print(df)
df.to_csv("cleantopcv.csv")