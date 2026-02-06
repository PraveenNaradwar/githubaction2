
import pandas as pd

print("extract data from mysql database")

data={
    "userid":[101,102,103],
    "name":['pooja','anil','sunil'],
    "age":[25,26,27]
}

df=pd.DataFrame(data)
print(df)