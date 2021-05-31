import csv
import pandas as pd
from pandas import DataFrame

df = pd.read_csv('venv/vieclam24h.csv')
print(df)

# company = df.iloc[:,1]
# title = df.iloc[:,0]
#
#
#
# title1 = []
# company1= []
# for i in company:
#
#     begin = i.find("]")
#
#
#     i = i[begin+1:]
#     company1.append(i)
# for j in title:
#     begin = j.find("]")
#
#     j = j[begin + 1:]
#
#     title1.append(j)
#
# title1= DataFrame(title1)
# company1 = DataFrame(company1)
# kq = pd.concat([title1, company1], axis=1)
#
# kq = pd.concat([kq,df.iloc[:,2],df.iloc[:,3],df.iloc[:,4],df.iloc[:,5],df.iloc[:,6],df.iloc[:,7]],axis=1)
# kq.to_csv("cleanybox.csv")
