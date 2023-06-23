import pandas as pd
import csv
df=pd.read_csv("brown_dwarfs.csv")
df.head()
df.dtypes
df=df.dropna()
df["radius"]=0.102763*df["radius"]
df["mass"]=0.000954588*df["mass"]
df.to_csv("new_dwarf_stars.csv")
with open("total_stars.csv","w",encoding="utf8")as f:
    csvwriter=csv.writer(f)
    
df=pd.read_csv("total_stars.csv")    
df.tail(8)